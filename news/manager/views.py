from django.shortcuts import render
from .models import News, Category
from .forms import NewsForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
# Create your views here.
def dashboard(request):

    latest = News.objects.all().order_by('-id')[:5]
    category = Category.objects.all().order_by('-id')[:8]
    dist = {
        'category':category,
        'latest':latest,

    }
    return render(request, "manager/dashboard.html", dist)

def news(request):
    latest = News.objects.all().order_by('-id')[:5]
   
    category = Category.objects.all().order_by('-id')[:8]
    form = NewsForm()
    dist = {
        'category':category,
        'latest':latest,
        'form':form,
    }
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        sav = form.save(commit= False)
        sav.added_by = request.user
        sav.save()
        messages.success(request, "सफलतापूर्वक समाचार थपियो")
    return render(request, "manager/news.html", dist)

def nowLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage:homepage'))