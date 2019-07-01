from django import forms
from django.contrib.auth import login
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.views.generic.edit import FormView

from conference.models import Presentation, Profile


class PresentationFrom(forms.ModelForm):
    class Meta:
        model = Presentation
        fields = ['title', 'description', 'datetime', 'room']

    def clean(self):
        room, datetime = self.cleaned_data['room'], self.cleaned_data['datetime']
        same_time_events = Presentation.objects.filter(room=room, datetime=datetime)
        if len(same_time_events) != 0:
            raise ValidationError('Selected room is being used at selected time')


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'birth_date']

    def clean(self):
        k = 0


class LoginForm(FormView):
    form_class = AuthenticationForm
    template_name = "index.html"
    success_url = "/profile/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super().form_valid(form)
