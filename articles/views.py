from django.shortcuts import render
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')


def dinner(request, name):
    menus = ['한식', '중식', '일식', '분식']
    pick = random.choice(menus)
    context = {
        'pick' : pick,
        'name' : name,
        'menus' : menus,
    }
    return render(request, 'dinner.html', context)


def dinner_price(request, name):
    menus = [{"name":'한식 정식',"price":30000}, {"name":'중식 정식',"price":20000}, {"name":'일식 정식',"price":70000}, {"name":'분식 정식',"price":8000}]
    pick = random.choice(menus)
    context = {
        'pick' : pick,
        'name' : name,
        'menus' : menus,
    }
    return render(request, 'dinner_price.html', context)