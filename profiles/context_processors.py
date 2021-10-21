from .models import Profile, Relationship, RelationshipManager


def profile_pic(request):
    if request.user.is_authenticated:
        profile_obj = Profile.objects.get(user=request.user)
        pic = profile_obj.avatar
        print(pic)
        return {"picture": pic}
    return {}


def invitations_received_no(request):
    if request.user.is_authenticated:
        profile_obj = Profile.objects.get(user=request.user)
        q_set_count = Relationship.objects.invitations_received(profile_obj).count()
        return {"invites_num": q_set_count}
    return {}

