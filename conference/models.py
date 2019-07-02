from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Room(models.Model):
    number = models.IntegerField()
    address = models.CharField(max_length=125)

    def __str__(self):
        return f"Room #{self.number} at {self.address}"


class Schedule(models.Model):
    room = models.OneToOneField(Room, on_delete=models.CASCADE, null=True, blank=True)

    @receiver(post_save, sender=Room)
    def create_room_schedule(sender, instance, created, **kwargs):
        if created:
            Schedule.objects.create(room=instance)

    def __str__(self):
        return f"Schedule for room #{self.room.number}"


class Presentation(models.Model):
    schedule = models.ForeignKey(Schedule, on_delete=models.CASCADE, blank=True, null=True)
    presenters = models.ManyToManyField(User, blank=True)
    datetime = models.DateTimeField()
    title = models.CharField(max_length=125)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    description = models.CharField(max_length=350, default="")

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        schedule = Schedule.objects.filter(room=self.room)[0]
        self.schedule = schedule
        self.save_base()

    def __str__(self):
        return f"Presentation {self.title}"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    attend_presentations = models.ManyToManyField(Presentation, blank=True)

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def __str__(self):
        return f"Profile {self.user.first_name} {self.user.last_name}"
