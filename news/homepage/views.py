from django.shortcuts import render
from manager.models import Category, SubCategory, News
# Create your views here.
def Homepage(request):
    category = Category.objects.all()
    template = 'news/homepage.html'
    news = News.objects.all().order_by('-id')[:6]
    hot = News.objects.all().order_by('-id')[:4]
    print(hot)
    latest = News.objects.all().order_by('-id')[:5]
    dist ={
        'category':category,
        'news':news,
        'latest':latest,
        'hot':hot
    }

    return render(request, template, dist)

def newsDetails(request, id, slug):
    news = News.objects.get(id = id)
    latest = News.objects.all().order_by('-id')[:5]
    category = Category.objects.all().order_by('-id')[:8]
    other = News.objects.all().order_by('?')[:10]
    dist = {
        'category':category,
        'news':news,
        'latest':latest,
        'other':other
    }

    return render(request, "news/news_details.html", dist)