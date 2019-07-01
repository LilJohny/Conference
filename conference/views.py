import datetime

import pytz
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView, CreateView, ListView, UpdateView, FormView
from django.views.generic.base import TemplateView

from conference.forms import PresentationFrom, ProfileForm
from conference.models import Presentation, Profile, Room


class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/accounts/login"
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        events = Presentation.objects.all().order_by('datetime')
        context['events'] = events.filter(datetime__gte=datetime.datetime.now())
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        if request.user.has_perm('conference.can_create_presentations'):
            context['creator'] = True
        else:
            context['creator'] = False
        return render(request, template_name=self.template_name, context=context)


class ProfileEditView(UpdateView):
    template_name = 'profile_update.html'
    model = Profile
    form_class = ProfileForm
    success_url = '/profile'

    def get_object(self, queryset=None):
        user = self.request.user
        return Profile.objects.filter(user=user)[0]


class ProfileDetailView(DetailView):
    model = Profile
    template_name = "profile_view.html"

    def get_object(self, queryset=None):
        user = self.request.user
        profile = Profile.objects.filter(user=user)[0]
        return profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.kwargs.get('user_id') is None:
            profile = Profile.objects.filter(user=self.request.user)[0]
        else:
            profile = Profile.objects.filter(user_id=self.kwargs['user_id'])[0]
        context['events'] = profile.attend_presentations.all()
        context['author_events'] = Presentation.objects.filter(presenter=profile.user)
        context['profile'] = profile
        context['user_id'] = self.request.user.id
        context['creator'] = profile.user.has_perm('conference.can_create_presentations')

        return context


class PresentationCreateView(CreateView):
    template_name = 'presentation_create.html'
    model = Presentation
    form_class = PresentationFrom

    def form_valid(self, form):
        title, description, datetime, room = form.cleaned_data['title'], form.cleaned_data['description'], \
                                             form.cleaned_data['datetime'], form.cleaned_data['room']
        user = User.objects.filter(username=self.request.user.username, password=self.request.user.password)[0]
        presentation = Presentation(presenter=user, title=title, description=description, datetime=datetime,
                                    room=room)
        presentation.save()

        return HttpResponseRedirect("/")


class PresentationUpdateView(UpdateView):
    template_name = 'presentation_update.html'
    model = Presentation
    fields = ['title', 'description', 'room', 'datetime']

    def get_object(self, queryset=None):
        event_id = self.kwargs['event_id']
        return Presentation.objects.filter()[0]

    def get_success_url(self):
        return f"/presentations/{self.object.event_id}"


class PresentationsListView(ListView):
    model = Presentation
    paginate_by = 20
    template_name = 'presentations_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['name'] = "My presentations"
        return context

    def get_queryset(self):
        user = User.objects.filter(username=self.request.user.username, password=self.request.user.password)[0]
        return Presentation.objects.filter(presenter=user)


class AllPresentationsListView(ListView):
    model = Presentation
    paginate_by = 10
    template_name = 'presentation_all.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['rooms'] = Room.objects.all()
        context['presentations'] = {}
        for room in context['rooms']:
            context['presentations'][room] = Presentation.objects.filter(room=room)
        context['creator'] = self.request.user.has_perm('conference.can_create_presentations')
        return context

    def get_queryset(self):
        return Presentation.objects.all()


class PresentationDetailView(DetailView):
    model = Presentation
    template_name = 'presentation_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = datetime.datetime.now()
        now = now.replace(tzinfo=pytz.UTC)
        time = self.object.datetime
        time = time.replace(tzinfo=pytz.UTC)
        context['can_attend'] = time > now
        current_user = self.request.user
        author = self.object.presenter
        context['signed_up'] = self.object.profile_set.filter(user=current_user).exists()
        if current_user.username == author.username and current_user.password == author.password:
            context['author'] = True
        else:
            context['author'] = False
        return context

    def get_object(self, queryset=None):
        event_id = self.kwargs.get("event_id")
        return Presentation.objects.filter(id=event_id)[0]


def room_schedule(request, room_number):
    events = Presentation.objects.filter(room__number=room_number)
    return render(request, 'room.html', {'room_number': room_number, 'events': events},
                  )


def event_signup(request, event_id):
    user = User.objects.filter(username=request.user.username, password=request.user.password)[0]
    presentation = Presentation.objects.filter(event_id=event_id)[0]
    profile_set = Profile.objects.filter(user=user)
    presentation.profile_set.set(presentation.profile_set.union(profile_set))
    presentation.save()
    return HttpResponseRedirect(f"/presentations/{event_id}")


def index(requset):
    return render(requset, 'index.html')

