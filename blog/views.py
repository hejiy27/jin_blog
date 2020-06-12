from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Post


def Posts_list(request):
    posts = Post.objects.all()

    return render(request, 'blogs/posts_list.html', context={'posts':posts})