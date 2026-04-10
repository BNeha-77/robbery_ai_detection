from django.test import TestCase
from django.contrib.auth.models import User
from .models import Profile

class ProfileModelTest(TestCase):
    def test_profile_creation(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        profile = Profile.objects.create(user=user, is_admin=False)
        self.assertEqual(profile.user.username, 'testuser')
