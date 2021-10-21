from django.db import models
from django.contrib.auth.models import User
from .utils import get_uid
from django.template.defaultfilters import slugify
from django.db.models import Q
from django.shortcuts import reverse


class ProfileManager(models.Manager):

    def get_all_profiles_to_invite(self, sender):
        profiles = Profile.objects.all().exclude(user=sender)
        profile = Profile.objects.get(user=sender)
        q_set = Relationship.objects.filter(Q(sender=profile) | Q(receiver=profile))
        accepted = set([])
        for rel_ship in q_set:
            if rel_ship.status == "accepted":
                accepted.add(rel_ship.receiver)
                accepted.add(rel_ship.sender)
        available = [profile for profile in profiles if profile not in accepted]
        return available

    def get_all_profiles(self, me):  # !!!
        profiles = Profile.objects.all().exclude(user=me)
        return profiles


class Profile(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(default="Bio is not completed...", max_length=400)
    country = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(default="avatar.png", upload_to="avatars/")
    following = models.ManyToManyField(User, blank=True, related_name="following")
    friends = models.ManyToManyField(User, blank=True, related_name="friends")
    slug = models.SlugField(unique=True, blank=True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    objects = ProfileManager()

    def __str__(self):
        return f"{self.user}-{self.created.strftime('%d-%m-%Y')}"

    def get_absolute_url(self):
        return reverse("profiles:profiles-detail-view", kwargs={"slug": self.slug})

    def get_friends(self):
        return self.friends.all()

    def get_followers(self):
        return self.following.all()

    def get_friends_number(self):
        return self.friends.all().count()

    def get_post_no(self):
        return self.posts.all().count()

    def get_all_authors_posts(self):
        return self.posts.all()

    def get_likes_given_no(self):
        likes = self.like_set.all()
        total_liked = 0
        for like in likes:
            if like.value == "like":
                total_liked += 1
        return total_liked

    def get_likes_received_no(self):
        posts = self.posts.all()
        total_liked = 0
        for like in posts:
            total_liked += like.liked.all().count()
        return total_liked

    __initial_first_name = None
    __initial_last_name = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initial_first_name = self.first_name
        self.__initial_last_name = self.last_name

    def save(self, *args, **kwargs):
        exist = False
        to_slug = self.slug
        if self.first_name != self.__initial_first_name or self.last_name != self.__initial_last_name or self.slug == "":
            if self.first_name and self.last_name:
                to_slug = slugify(str(self.first_name) + " " + str(self.last_name))
                exist = Profile.objects.filter(slug=to_slug).exists()
                while exist:
                    to_slug = slugify(to_slug + " " + str(get_uid()))
                    exist = Profile.objects.filter(slug=to_slug).exists()
            else:
                to_slug = str(self.user)
        self.slug = to_slug
        super().save(*args, **kwargs)


STATUS_CHOICES = (
    ("send", "send"),
    ("accepted", "accepted")
)


class RelationshipManager(models.Manager):  # !!!

    def invitations_received(self, receiver):
        q_set = Relationship.objects.filter(receiver=receiver, status="send")
        return q_set


class Relationship(models.Model):  # !!!
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="receiver")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = RelationshipManager()  # !!!

    def __str__(self):
        return f"{self.sender}, {self.receiver}, {self.status} at {self.updated.strftime('%d-%m-%Y - %H:%M')}"
