from django.shortcuts import render
from django.http import HttpResponse

import random


def home(request):
    return render(request, 'generator/home.html', { 'password' : 'kuch bhi' })

def password(request):

    length = request.GET.get('length')
    length = int(length)

    uppercase_pref = request.GET.get('uppercase')
    numbers_pref = request.GET.get('numbers')
    specials_pref = request.GET.get('specials')

    characters = list('abcdefghijklmnopqrstuvwxyz')
    uppercase = list('abcdefghijklmnopqrstuvwxyz'.upper())
    numbers = [ str(x) for x in range(10) ]
    specials = list('!@#$%^&*_')

    sample_space = characters

    if uppercase_pref:
        sample_space += uppercase
    
    if numbers_pref:
        sample_space += numbers
    
    if specials_pref:
        sample_space += specials


    generated_password = ''

    for _ in range(length):
        generated_password += random.choice(sample_space)

    return render(request, 'generator/password.html', {'password' : generated_password})


def about(request):
    return render(request, 'generator/about.html')