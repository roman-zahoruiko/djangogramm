from django.shortcuts import render, redirect
from .models import Post, Like
from profiles.models import Profile
from .forms import PostModelForm, CommentModelForm
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from itertools import chain


@login_required()
def posts_of_following_profiles(request):
    profile = Profile.objects.get(user=request.user)
    c_form = CommentModelForm()
    users = [user for user in profile.following.all()]
    following_posts = []
    q_set = None
    for user in users:
        p_profile = Profile.objects.get(user=user)
        profile_posts = p_profile.posts.all()
        following_posts.append(profile_posts)
    if len(following_posts) > 0:
        q_set = sorted(chain(*following_posts), reverse=True, key=lambda obj: obj.created)
    if "submit_c_form" in request.POST:
        c_form = CommentModelForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.user = profile
            instance.post = Post.objects.get(id=request.POST.get("post_id"))
            instance.save()
            c_form = CommentModelForm()
            # return redirect("posts:main-post-view")
    context = {
        "q_set": q_set,
        "profile": profile,
        "c_form": c_form,
    }
    return render(request, "posts/following.html", context)


@login_required()
def post_comment_create_and_list_view(request):
    q_set = Post.objects.all()
    p_form = PostModelForm()
    c_form = CommentModelForm()
    post_added = False
    profile = Profile.objects.get(user=request.user)

    if "submit_p_form" in request.POST:
        p_form = PostModelForm(request.POST, request.FILES)
        if p_form.is_valid():
            instance = p_form.save(commit=False)
            instance.author = profile
            instance.save()
            p_form = PostModelForm()
            post_added = True
            # return redirect("posts:main-post-view")
    if "submit_c_form" in request.POST:
        c_form = CommentModelForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.user = profile
            instance.post = Post.objects.get(id=request.POST.get("post_id"))
            instance.save()
            c_form = CommentModelForm()
            return redirect("posts:main-post-view")
    context = {
        "q_set": q_set,
        "profile": profile,
        "p_form": p_form,
        "c_form": c_form,
        "post_added": post_added,
    }
    return render(request, "posts/main.html", context)


@login_required()
def like_dislike_posts(request):
    if request.method == "POST":
        post_id = request.POST.get("post_id")
        post_obj = Post.objects.get(id=post_id)
        profile = Profile.objects.get(user=request.user)
        if profile in post_obj.liked.all():
            post_obj.liked.remove(profile)
        else:
            post_obj.liked.add(profile)
        like, created = Like.objects.get_or_create(user=profile, post_id=post_id)
        if not created:
            if like.value == "Like":
                like.value = "Dislike"
            else:
                like.value = "Like"
        else:
            like.value = "Like"
        post_obj.save()
        like.save()
        data = {
            "value": like.value,
            "like": post_obj.liked.all().count()
        }
        return JsonResponse(data, safe=False)

    return redirect("posts:main-post-view")


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name = "posts/confirm_del.html"
    success_url = reverse_lazy("posts:main-post-view")

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get("pk")
        obj = Post.objects.get(pk=pk)
        if not obj.author.user == self.request.user:
            messages.warning(self.request, "You need to be the author of the post to delete it!")
        return obj


class PostUpdateView(LoginRequiredMixin, UpdateView):
    form_class = PostModelForm
    model = Post
    template_name = "posts/update.html"
    success_url = reverse_lazy("posts:main-post-view")

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        if form.instance.author == profile:
            return super().form_valid(form)
        else:
            form.add_error(None, "You need to be the author of the post to update it!")
            return super().form_invalid(form)
