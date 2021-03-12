# request - пользователь отправляет запрос
from django.http import HttpResponse
from django.shortcuts import render


# Новая страница
def about(request):
    return HttpResponse('This is about page')


# Новая страница
def home(request):
    # Не очень
    # return HttpResponse('<h1>This page was made by: _Counter021_</h1>')
    # Первый параметр request обязательно
    # Второй файл с html кодом
    # Можно 3 - словарь (python код)
    return render(request, 'home.html', {'greeting': 'Hello!'})
