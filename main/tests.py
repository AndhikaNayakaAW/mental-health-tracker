from django.test import TestCase, Client
from django.utils import timezone
from .models import MoodEntry
from django.contrib.auth.models import User

class MainTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='andhika.nayaka', password='nayganteng12')

    def test_main_template_uses_correct_page_title(self):
        # Log in the client
        self.client.login(username='andhika.nayaka', password='nayganteng12')

        self.client.cookies['last_login'] = '2024-09-20 10:00:00'


        # Now get the response
        response = self.client.get("/")
        html_response = response.content.decode("utf8")

        # Check if the title is present
        self.assertIn("PBD Mental Health Tracker", html_response)