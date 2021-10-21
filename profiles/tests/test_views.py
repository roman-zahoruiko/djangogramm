from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])
        self.my_profile_url = reverse("profiles:my-profile-view")
        self.profiles_list_view_url = reverse("profiles:all-profiles-view")
        self.invites_received_view_url = reverse("profiles:my-invites-view")

    def test_my_profile_url(self):
        response = self.client.get(self.my_profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/myprofile.html")

    def test_profiles_list_view_url(self):
        response = self.client.get(self.profiles_list_view_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/profile_list.html")

    def test_invites_received_view_url(self):
        response = self.client.get(self.invites_received_view_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "profiles/my_invites.html")
