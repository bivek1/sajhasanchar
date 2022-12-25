from django.shortcuts import render
from manager.models import Category, SubCategory, News
from django.contrib.auth import authenticate
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login
from django.http import HttpResponseRedirect
# Create your views here.
def Homepage(request):
    category = Category.objects.all()
    template = 'news/homepage.html'
    news = News.objects.all().order_by('-id')[:13]
    normal = News.objects.filter(status = 'Normal').order_by('-id')[:12]
    hot = News.objects.filter(status = 'Hot').order_by('-id')[:12]
    print(hot)
    latest = News.objects.all().order_by('-id')[:20]
    watched = News.objects.all().order_by('-total_visit')[:15]
    dist ={
        'category':category,
        'news_all':news,
        'latest':latest,
        'hot':hot,
        'normal':normal,
        'watched':watched
    }

    return render(request, template, dist)

def newsDetails(request, id):
    news = News.objects.get(id = id)
    
    latest = News.objects.all().order_by('-id')[:11]
    category = Category.objects.all().order_by('-id')[:10]
    other = News.objects.all().order_by('?')[:10]
   
    dist = {
        'category':category,
        'news_all':news,
        'latest':latest,
        'other':other
    }
    news.total_visit += 1
    news.save()

    return render(request, "news/news_details.html", dist)

def Login(request):
    template_name = "manager/login.html"
    latest = News.objects.all().order_by('-id')[:11]
    category = Category.objects.all().order_by('-id')[:10]
    dist = {
        'category':category,
        'latest':latest,
    }
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        use = authenticate(request, username = username, password = password)
        if use is not None:
            login(request, use)
            return HttpResponseRedirect(reverse('manager:dashboard'))
        else:
            messages.error(request, "Incorrect Username and Password")
            return render(request, template_name, dist)
    
    return render(request, template_name,dist)
   
def selectNews(request, str):
    category = Category.objects.all()[:10]
    template = 'news/select_news.html'
    news = News.objects.filter(status = str).order_by('-id')
    hot = News.objects.filter(status = 'Hot').order_by('-id')[:10]
   
    normal = News.objects.filter(status = 'Normal').order_by('-id')[:10]
    latest = News.objects.all().order_by('-id')[:15]
    dist ={
        'category':category,
        'news_all':news,
        'latest':latest,
        'hot':hot,
        'selected':str,
        'normal':normal
    }

    return render(request, template, dist)


def categoryNews(request, id, slug):
    category = Category.objects.all()[:10]
    cat = Category.objects.get(id = id)
    template = 'news/category_news.html'
    news = News.objects.filter(category = cat).order_by('-id')
 
    normal = News.objects.filter(status = 'Normal').order_by('-id')[:10]
    latest = News.objects.all().order_by('-id')[:15]
    dist ={
        'category':category,
        'news_all':news,
        'latest':latest,
        'cat':cat,
       
        'normal':normal
    }

    return render(request, template, dist)