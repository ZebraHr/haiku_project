from django.http import HttpResponse
from django.shortcuts import render

from .models import Post


def index(request):
    """Главная страница."""
    posts = Post.objects.all()[:10]
    # page_obj = pagination(request, posts)
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context)


def profile(request, username):
    '''Страница профиля.'''
    ...