from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    """Главная страница."""
    return render(request, 'posts/index.html')


def profile(request, username):
    '''Страница профиля.'''
    ...