from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request,'index.html')
def password(request):

    character=list('abcdefghijklmnopqrstuvwxyz')
    length=int(request.POST.get('length'))
    password=''
    upper= request.POST.get('upper')
    special=request.POST.get('special')
    number=request.POST.get('numbers')
    if upper=='on':
        character.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    elif special=='on':
        character.extend(list('~!@#$%^&*{}[];\|:<(>?/)'))
    elif number=='on':
        character.extend(list(str('1234567890')))
    for i in range(0,length):
        password += random.choice(character)



    return render(request,'password.html',{'password':password})