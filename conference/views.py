from django.shortcuts import render
from conference.models import Presentation
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView


class Home(TemplateView):
    template_name = 'index.html'

    # additional_context = get_latest_events()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        events = Presentation.objects.all()
        context['events'] = events.order_by('datetime')
        return context


def room_schedule(request, room_number):
    events = Presentation.objects.filter(room__number=room_number)
    return render(request, 'room.html', {'room_number': room_number, 'events': events},
                  )


def login(request):
    username = request.GET['username']
    password = request.GET['psw']
    user = User.objects.filter(username=username, password=password)
    k = 0


def index(requset):
    return render(requset, 'index.html')
