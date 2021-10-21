from django.urls import path
from .views import (
    my_profile_view, invites_received_view, invite_profiles_list_view, ProfilesListView, follow_unfollow_profile,
    ProfilesDetailView, send_invitation, accept_invitation, reject_invitation, remove_from_friends, profile_subs_view,
    search_result
)


app_name = "profiles"

urlpatterns = [
    path("", ProfilesListView.as_view(), name="all-profiles-view"),
    path("search/", search_result, name="search"),
    path("myprofile/", my_profile_view, name="my-profile-view"),
    path("my-invites/", invites_received_view, name="my-invites-view"),
    path("to-invite/", invite_profiles_list_view, name="invite-profiles-view"),
    path("send-invite/", send_invitation, name="send-invite"),
    path("remove-friend/", remove_from_friends, name="remove-friend"),
    path("switch_follow/", follow_unfollow_profile, name="follow-unfollow-view"),
    path("my-subscriptions/", profile_subs_view, name="my-subscriptions"),
    path("<slug>/", ProfilesDetailView.as_view(), name="profiles-detail-view"),
    path("my-invites/accept/", accept_invitation, name="accept-invite"),
    path("my-invites/reject/", reject_invitation, name="reject-invite"),
]

