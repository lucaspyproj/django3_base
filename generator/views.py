from django.shortcuts import render
from django.http import HttpResponse
import random
import string


def home(request):
    return render(request, 'generator/home.html', {'password':'huddfduenc'})


def password(request):

    characters = string.ascii_lowercase
    
    if request.GET.get('uppercase'):
        characters += string.ascii_uppercase
    if request.GET.get('numbers'):
        characters += string.digits
    if request.GET.get('special'):
        characters += string.punctuation

    length = int(request.GET.get('length', 12))

    passwd = ''
    for _ in range(length):
        passwd += random.choice(characters)

    return render(request, 'generator/password.html', {'password': passwd})

def about(request):
    return render(request, 'generator/about.html')