from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import SocialPost
from .forms import SocialPostForm


def home(request):
    return redirect("dashboard")


def dashboard(request):
    return render(request, "dashboard.html")


def post_list(request):
    posts = SocialPost.objects.all().order_by("-created_at")
    return render(request, "posts/list.html", {"posts": posts})


def post_create(request):
    if request.method == "POST":
        form = SocialPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            if request.user.is_authenticated:
                post.author = request.user
            post.save()
            messages.success(request, "Post created.")
            return redirect("post_list")
    else:
        form = SocialPostForm()
    return render(request, "posts/form.html", {"form": form, "mode": "Create"})


def post_update(request, pk):
    post = get_object_or_404(SocialPost, pk=pk)
    if request.method == "POST":
        form = SocialPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated.")
            return redirect("post_list")
    else:
        form = SocialPostForm(instance=post)
    return render(request, "posts/form.html", {"form": form, "mode": "Edit"})


def post_delete(request, pk):
    post = get_object_or_404(SocialPost, pk=pk)
    if request.method == "POST":
        post.delete()
        messages.success(request, "Post deleted.")
        return redirect("post_list")
    return render(request, "posts/confirm_delete.html", {"post": post})

