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
    news = News.objects.all().order_by('-id')[:6]
    hot = News.objects.all().order_by('-id')[:4]
    print(hot)
    latest = News.objects.all().order_by('-id')[:5]
    dist ={
        'category':category,
        'news_all':news,
        'latest':latest,
        'hot':hot
    }

    return render(request, template, dist)

def newsDetails(request, id):
    news = News.objects.get(id = id)
    latest = News.objects.all().order_by('-id')[:5]
    category = Category.objects.all().order_by('-id')[:8]
    other = News.objects.all().order_by('?')[:10]
    dist = {
        'category':category,
        'news_all':news,
        'latest':latest,
        'other':other
    }

    return render(request, "news/news_details.html", dist)

def Login(request):
    template_name = "manager/login.html"
    latest = News.objects.all().order_by('-id')[:5]
    category = Category.objects.all().order_by('-id')[:8]
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
   