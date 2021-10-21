from django.test import SimpleTestCase
from django.urls import reverse, resolve
from posts.views import (
    post_comment_create_and_list_view, posts_of_following_profiles, PostUpdateView, like_dislike_posts
)


class TestUrls(SimpleTestCase):

    def test_main_post_view_is_resolved(self):
        url = reverse("posts:main-post-view")
        self.assertEqual(resolve(url).func, post_comment_create_and_list_view)

    def test_following_post_view_is_resolved(self):
        url = reverse("posts:follow-post-view")
        self.assertEqual(resolve(url).func, posts_of_following_profiles)

    def test_post_update(self):
        url = reverse("posts:post-update", args=["123"])
        self.assertEqual(resolve(url).func.view_class, PostUpdateView)

    def test_post_like_dislike(self):
        url = reverse("posts:like-post-view")
        self.assertEqual(resolve(url).func, like_dislike_posts)