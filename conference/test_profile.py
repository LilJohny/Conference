from unittest import TestCase
from django.contrib.auth.models import User
from conference.models import Profile


class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username='Test', password='testpassword')
        self.user.save()

    def test_create_user_profile(self):
        self.assertEquals(Profile.objects.filter(user=self.user).count(), 1)

    def tearDown(self):
        self.user.delete()
