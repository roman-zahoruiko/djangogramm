from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from posts.models import Post
from profiles.models import Profile


class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])
        self.profile = Profile.objects.get(user=1)
        self.posts_url = reverse("posts:main-post-view")
        self.following_url = reverse("posts:follow-post-view")
        self.post_update_url = reverse("posts:post-update", args=["1"])
        self.post_1 = Post.objects.create(
            content="test",
            author=self.profile
        )

    def test_post_list(self):
        response = self.client.get(self.posts_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/main.html")

    def test_following_list(self):
        response = self.client.get(self.following_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/following.html")

    def test_post_update(self):
        response = self.client.get(self.post_update_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "posts/update.html")
