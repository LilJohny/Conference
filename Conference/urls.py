"""Conference URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from conference.views import room_schedule, HomeView, PresentationCreateView, PresentationDetailView, \
    PresentationsListView, PresentationUpdateView, RegisterFormView, event_signup, ProfileDetailView, ProfileEditView, \
    AllPresentationsListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('rooms/<int:room_number>/', room_schedule),
    path('', HomeView.as_view(), name='home'),
    path('profile', ProfileDetailView.as_view()),
    path('profile/<int:user_id>', ProfileDetailView.as_view()),
    path('profile/edit', ProfileEditView.as_view()),
    path('accounts/register/', RegisterFormView.as_view(), name='register'),
    path('presentations/all', AllPresentationsListView.as_view()),
    path('presentations/create', PresentationCreateView.as_view()),
    path('presentations/<int:event_id>', PresentationDetailView.as_view()),
    path('presentations/my', PresentationsListView.as_view()),
    path('presentations/<int:event_id>/edit', PresentationUpdateView.as_view()),
    path('presentations/<int:event_id>/signup', event_signup)
]

