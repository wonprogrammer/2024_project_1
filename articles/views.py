from django.shortcuts import render
import random
from .models import Article

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
    articles = Article.objects.all()
    context = {
        'pick' : pick,
        'name' : name,
        'menus' : menus,
        'articles'  :articles,
    }
    return render(request, 'dinner_price.html', context)


def review(request):
    return render(request, 'review.html')


def create_review(request):
    content = request.POST.get('content')
    print(request.POST)
    context = {
        'content' : content,
    }
    return render(request, 'review_result.html', context)