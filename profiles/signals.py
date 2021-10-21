from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile, Relationship


@receiver(post_save, sender=User)
def post_save_new_profile(sender, instance, created, **kwargs):
    """Create a profile when adding a user."""
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=Relationship)
def post_save_add_to_friends(sender, instance, created, **kwargs):
    request_sender = instance.sender
    request_receiver = instance.receiver
    if instance.status == "accepted":
        request_sender.friends.add(request_receiver.user)
        request_receiver.friends.add(request_sender.user)
        request_sender.save()
        request_receiver.save()


@receiver(pre_delete, sender=Relationship)
def pre_delete_remove_from_friends(sender, instance, **kwargs):
    request_sender = instance.sender
    request_receiver = instance.receiver
    request_sender.friends.remove(request_receiver.user)
    request_receiver.friends.remove(request_sender.user)
    request_sender.save()
    request_receiver.save()

