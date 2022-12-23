from django.shortcuts import render
from manager.models import Category, SubCategory, News
# Create your views here.
def Homepage(request):
    category = Category.objects.all()
    template = 'news/homepage.html'
    news = News.objects.all().order_by('-id')[:6]
    hot = News.objects.all()[:4]
    print(hot)
    dist ={
        'category':category,
        'news':news,
        'hot':hot
    }

    return render(request, template, dist)