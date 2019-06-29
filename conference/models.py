from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import uuid


class Schedule(models.Model):
    pass


class Room(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE)
    number = models.IntegerField()
    address = models.CharField(max_length=125)
    room_id = models.CharField(max_length=39, blank=True)

    def __str__(self):
        return f"Room#{self.number} at {self.address}"

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.room_id = str(uuid.uuid3(uuid.NAMESPACE_OID, str(self.number) + str(self.address)).int)
        self.save_base()


class Presentation(models.Model):
    presenter = models.ForeignKey(User, on_delete=models.CASCADE)
    datetime = models.DateTimeField()
    title = models.CharField(max_length=125)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    description = models.CharField(max_length=350, default="")
    event_id = models.CharField(max_length=39, blank=True)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        self.event_id = str(uuid.uuid3(uuid.NAMESPACE_OID, str(self.datetime) + str(self.room.room_id)).int)
        self.save_base()


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    attend_presentations = models.ForeignKey(Presentation, on_delete=models.PROTECT, null=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
