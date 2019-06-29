from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login


class RegisterForm(FormView):
    form_class = UserCreationForm
    success_url = "/login"
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LoginForm(FormView):
    form_class = AuthenticationForm
    template_name = "index.html"
    success_url = "/profile/"

    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super().form_valid(form)


