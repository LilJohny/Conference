from rest_framework import serializers
from .models import Schedule, Room, Presentation
from django.contrib.auth.models import User, Group


class PresentationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Presentation
        fields = ['title', 'description', 'datetime', 'room', 'presenters']
        depth = 1


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name')


class RoomSerializer(serializers.ModelSerializer):
    number = serializers.IntegerField()
    address = serializers.CharField()
    presentation_set = PresentationSerializer(many=True)

    class Meta:
        model = Room
        fields = ['number', 'address', 'presentation_set']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['name']


class ScheduleSerializer(serializers.HyperlinkedModelSerializer):
    room = RoomSerializer(many=False)

    class Meta:
        model = Schedule
        fields = ['room']
        depth = 4
