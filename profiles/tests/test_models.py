from django.test import TestCase, Client
from django.contrib.auth.models import User
from posts.models import Post
from profiles.models import Profile


class TestModels(TestCase):

    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])
        self.profile = Profile.objects.get(user=1)
        self.post_1 = Post.objects.create(
            content="test",
            author=self.profile
        )

    def test_slug_on_create(self):
        self.assertEqual(self.profile.slug, "testuser")

    def test_posts_qnt(self):
        self.assertEqual(self.profile.get_post_no(), 1)

    def test_profile_url(self):
        self.assertEqual(self.profile.get_absolute_url(), '/profiles/testuser/')

    def test_likes_received(self):
        self.assertEqual(self.profile.get_likes_received_no(), 0)

    def test_likes_given(self):
        self.assertEqual(self.profile.get_likes_given_no(), 0)
