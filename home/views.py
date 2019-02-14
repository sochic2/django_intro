from django.shortcuts import render, HttpResponse
import random
from datetime import datetime
# from pprint import pprint

# Create your views here.
def index(request):
    # print(request)
    # print(type(request))
    # pprint(request.META)
    # return HttpResponse('Welcome to Django !')
    return render(request, 'home/index.html')

def dinner(request):
    menus = ['밥', '국', '면', '찌개', '왕밤빵']
    pick = random.choice(menus)
    return render(request, 'home/dinner.html', {'menus':menus, 'pick':pick})
    
def hello(request, name):
    return render(request, 'home/hello.html', {'name':name})
    
def cube(request, number):
    thnum = number **3
    return render(request, 'home/cube.html', {'number':number, 'thnum':thnum})
    
def ping(request):
    return render(request, 'home/ping.html')

def pong(request):
    print(request.GET)
    data = request.GET.get('data')
    return render(request, 'home/pong.html', {'data':data})

def user_new(request):
    return render(request, 'home/user_new.html')
    
def user_create(request):
    nickname = request.POST.get('nickname')
    password = request.POST.get('password')
    return render(request, 'home/user_create.html', {'password':password, 'nickname':nickname})
    
def template_example(request):
    my_list = ['짜장면', '탕수육', '짬뽕', '양장피']
    my_sentence = 'Life is short, you need python'
    messages = ['apple', 'dog', 'banana', 'cherry', 'melon', 'cat']
    empty_list = []
    datetimenow = datetime.now()
    return render(request, 'home/template_example.html', 
                {'my_list':my_list, 'my_sentence' : my_sentence,
                    'messages' : messages, 'empty_list' : empty_list,
                    'datetimenow':datetimenow
                })
                
def static_example(request):
    return render(request, 'home/static_example.html')
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    