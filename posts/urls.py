from django.urls import path
from .views import (post_comment_create_and_list_view, like_dislike_posts,
                    PostDeleteView, PostUpdateView, posts_of_following_profiles)


app_name = "posts"
urlpatterns = [
    path("", post_comment_create_and_list_view, name="main-post-view"),
    path("following/", posts_of_following_profiles, name="follow-post-view"),
    path("liked/", like_dislike_posts, name="like-post-view"),
    path("<pk>/delete/", PostDeleteView.as_view(), name="post-delete"),
    path("<pk>/update/", PostUpdateView.as_view(), name="post-update"),
]
