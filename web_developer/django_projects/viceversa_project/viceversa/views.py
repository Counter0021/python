from django.shortcuts import render
from collections import Counter


# Домашняя страница
def home(request):
    return render(request, 'home.html')


# Буквы наоборот
def reverse(request):
    user_text = request.GET['usertext']
    elements = Counter(user_text.split(' '))
    sum_elements = sum(elements.values())
    sum_letter_in_words = sum(Counter(user_text.replace(' ', '')).values())
    reversed_text = user_text[::-1]
    return render(request, 'reverse.html',
                  {'usertext': user_text, 'reversed_text': reversed_text, 'sum_elements': sum_elements,
                   'letter_in_words': sum_letter_in_words
                   })
