from unittest import TestCase
from conference.models import Room, Schedule


class TestSchedule(TestCase):
    def setUp(self):
        self.room = Room(number=1, address='test_address')

    def create_room_schedule(self):
        self.assertEquals(Schedule.objects.filter(user=self.room).count(), 1)

    def tearDown(self):
        self.room.delete()
