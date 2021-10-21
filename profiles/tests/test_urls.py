from django.test import SimpleTestCase
from django.urls import reverse, resolve
from profiles.views import ProfilesListView, my_profile_view, ProfilesDetailView


class TestUrls(SimpleTestCase):

    def test_profile_list_view(self):
        url = reverse("profiles:all-profiles-view")
        self.assertEqual(resolve(url).func.view_class, ProfilesListView)

    def test_my_profile_view(self):
        url = reverse("profiles:my-profile-view")
        self.assertEqual(resolve(url).func, my_profile_view)

    def test_profile_detail_view(self):
        url = reverse("profiles:profiles-detail-view", args=["123"])
        self.assertEqual(resolve(url).func.view_class, ProfilesDetailView)
