from django.shortcuts import render
from django.http import HttpResponse

from blog.models import Post


def home(request, *args, **kwargs):
    context = {
        "posts": Post.objects.all()
    }
    return render(request, 'home.html', context)


def about(request, *args, **kwargs):
    context = {"title": "About"}
    return render(request, 'about.html', context)
