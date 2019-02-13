from django.shortcuts import render, HttpResponse
import random
# from pprint import pprint
# Create your views here.
def index(request):
    # print(request)
    # print(type(request))
    # pprint(request.META)
    return HttpResponse('Welcome to Django !')

def dinner(request):
    menus = ['밥', '국', '면', '찌개', '왕밤빵']
    pick = random.choice(menus)
    return render(request, 'dinner.html', {'menus':menus, 'pick':pick})
    
def hello(request, name):
    return render(request, 'hello.html', {'name':name})
    
def cube(request, number):
    thnum = number **3
    return render(request, 'cube.html', {'number':number, 'thnum':thnum})
    
def ping(request):
    return render(request, 'ping.html')

def pong(request):
    print(request.GET)
    data = request.GET.get('data')
    return render(request, 'pong.html', {'data':data})

def user_new(request):
    return render(request, 'user_new.html')
    
def user_create(request):
    nickname = request.POST.get('nickname')
    password = request.POST.get('password')
    return render(request, 'user_create.html', {'password':password, 'nickname':nickname})
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    