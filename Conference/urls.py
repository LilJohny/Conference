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
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from conference.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
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
    path('presentations/<int:event_id>/signup', event_signup),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('schedules/', ScheduleList.as_view(), name='schedules-list'),
    path('schedules/<int:pk>/', ScheduleDetail.as_view(), name='schedule-detail'),
    path('rooms/<int:pk>/', RoomDetail.as_view(), name='room-detail'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
    path('groups/<int:pk>', GroupDetail.as_view(), name='group-detail')

]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
