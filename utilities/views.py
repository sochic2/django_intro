from django.shortcuts import render
from datetime import datetime
import json
import os
import requests


now_time = datetime.now()
# Create your views here.
def index(request):
    return render(request, 'utilities/index.html')

def bye(request):
    bye_time = datetime(2019, 2, 28)
    
    remain_time = bye_time - now_time
    return render(request, 'utilities/bye.html', {'bye_time':bye_time, 'remain_time':remain_time})
    
def graduation(request):
    graduation_time = datetime(2019, 5, 20)
    remain_g_time = graduation_time - now_time
    return render(request, 'utilities/graduation.html', {'graduation_time':graduation_time, 'remain_g_time':remain_g_time})
    
def imagepick(request):
    return render(request, 'utilities/imagepick.html')
    
def today(request):
    hidden_token=os.getenv('token1')
    url = f'https://api.openweathermap.org/data/2.5/weather?q=Daejeon,kr&lang=kr&APPID={hidden_token}'
    d = requests.get(url)
    r = d.json()
    description = r["weather"][0]["description"]
    city_name = r["name"]
    degree = int(r["main"]["temp"])-273
    return render(request, 'utilities/today.html', {'description':description,
        'city_name':city_name, 'degree':degree, 'now_time':now_time})


def ascii_new(request):
    return render(request, 'utilities/ascii_new.html')

def ascii_make(request):
    data = request.GET.get('data')
    value = request.GET.get('value')
    url = requests.get(f'http://artii.herokuapp.com/make?text={data}&font={value}').text
    return render(request, 'utilities/ascii_make.html', 
                {'url': url})

def original(request):
    return render(request, 'utilities/original.html')
    
def translated(request):
    return render(request, 'utilities/translated.html')
    

