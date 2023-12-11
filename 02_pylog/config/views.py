from django.shortcuts import render
from blog.models import Post


def index(request):
    return render(request, "index.html")


def post_list(request):
    posts = Post.objects.all()

    context = {
        "posts": posts
    }

    return render(request, "post_list.html", context)
