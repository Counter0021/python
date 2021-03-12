# request - пользователь отправляет запрос
from django.http import HttpResponse


def about(request):
    return HttpResponse('This is about page')


def home(request):
    # Не очень
    return HttpResponse('<h1>This page was made by: _Counter021_</h1>')
