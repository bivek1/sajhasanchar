from django.shortcuts import render
from .models import News, Category, SubCategory
from .forms import NewsForm, CategoryForm, SubCategoryForm, UserForm, PasswordChangeFormUpdate
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import logout
import datetime
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
# Create your views here.
def dashboard(request):

    latest = News.objects.all().order_by('-id')[:5]
    category = Category.objects.all().order_by('-id')[:8]
    taja = News.objects.filter(status='Hot')
    pachilo = News.objects.filter(status='Latest')
    trending = News.objects.filter(status='Trending')
    anya = News.objects.filter(status='Normal')


    dist = {
        'category':category,
        'latest':latest,
        'taja':taja.count(),
        'all_news':News.objects.all().order_by('-id')[:10],
        'all_news_count':News.objects.all().count(),
        'pachilo':pachilo.count(),
        'trending':trending.count(),
        'anya':anya.count(),
        'taja_today':taja.filter(created_at__date = datetime.date.today()).count(),
        'pachilo_today':pachilo.filter(created_at__date = datetime.date.today()).count(),
        'trending_today':trending.filter(created_at__date = datetime.date.today()).count(),
        'anya_today':anya.filter(created_at__date = datetime.date.today()).count()

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
        if form.is_valid():
            sav = form.save(commit= False)
            sav.added_by = request.user
            sav.save()
            messages.success(request, "सफलतापूर्वक समाचार थपियो")
        else:
            messages.success(request, "पोस्ट गर्न समस्या छ")
    return render(request, "manager/news.html", dist)


def allNews(request):
    latest = News.objects.all().order_by('-id')[:5]
    category = Category.objects.all().order_by('-id')[:8]
    all_news = News.objects.all().order_by('-id')

    dist = {
        'category':category,
        'latest':latest,
        'all_news':all_news
    }
    return render(request,'manager/allNews.html', dist)

def cnews(request, str):
    latest = News.objects.all().order_by('-id')[:5]
    category = Category.objects.all().order_by('-id')[:8]
    all_news = News.objects.filter(status = str).order_by('-id')

    dist = {
        'category':category,
        'latest':latest,
        'all_news':all_news,
        'status':str
    }
    return render(request,'manager/c_news.html', dist)


def deleteNews(request, id):
    news = News.objects.get(id = id)
    news.delete()

    messages.success(request, "तपाईंको समाचार मेटाइएको छ")
    return HttpResponseRedirect(reverse('manager:allNews'))


def updateNews(request, id):
    latest = News.objects.all().order_by('-id')[:5]
    
    category = Category.objects.all().order_by('-id')[:8]
    news = News.objects.get(id = id)
    form = NewsForm(instance=news)
    
    dist = {
        'category':category,
        'latest':latest,
        'form':form,
        'real_news':news
    }
    if request.method == 'POST':
        
        form = NewsForm(request.POST, request.FILES, instance= news)
        if form.is_valid():
            sav = form.save(commit= False)
            sav.added_by = request.user
            sav.save()
            messages.success(request, "सफलतापूर्वक समाचार अद्यावधिक गरियो")
        else:
            messages.success(request, "पोस्ट अद्यावधिक गर्न समस्या छ")
        return HttpResponseRedirect(reverse('manager:allNews'))
    return render(request, "manager/editNews.html", dist)


def CategoryView(request):
    latest = News.objects.all().order_by('-id')[:5]
    category = Category.objects.all().order_by('-id')[:8]
    form = CategoryForm()
    all_category = Category.objects.all().order_by('-id')
    dist = {
        'category':category,
        'latest':latest,
        'form':form,
        'all_category':all_category
    }
    if request.method == 'POST':
        edit_id = None
        try:
            edit_id = request.POST['edit']
            news_real = Category.objects.get(id = edit_id)
            print(news_real)
            form = CategoryForm(request.POST, request.FILES, instance=news_real)
            if form.is_valid():
                form.save()
                messages.success(request, "सफलतापूर्वक अद्यावधिक गरियो")
            else:
                messages.success(request, "पोस्ट अद्यावधिक गर्न समस्या छ")
        except:
            form = CategoryForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "सफलतापूर्वक कोटि थपियो")
            else:
                messages.success(request, "पोस्ट गर्न समस्या छ")

    return render(request, "manager/category.html", dist)

def deleteCategory(request , id):
    cate = Category.objects.get(id = id)
    cate.delete()
    messages.success(request, "तपाईंको कोटि मेटाइएको छ")
    return HttpResponseRedirect(reverse('manager:category'))



def subCategoryView(request):
    latest = News.objects.all().order_by('-id')[:5]
    category = Category.objects.all().order_by('-id')[:8]
    form = SubCategoryForm()
    all_category = SubCategory.objects.all().order_by('-id')
    dist = {
        'category':category,
        'latest':latest,
        'form':form,
        'all_category':all_category
    }
    if request.method == 'POST':
        edit_id = None
        try:
            edit_id = request.POST['edit']
            news_real = SubCategory.objects.get(id = edit_id)
            print(news_real)
            form = SubCategoryForm(request.POST, request.FILES, instance=news_real)
            if form.is_valid():
                form.save()
                messages.success(request, "सफलतापूर्वक अद्यावधिक गरियो")
            else:
                messages.success(request, "पोस्ट अद्यावधिक गर्न समस्या छ")
        except:
            form = SubCategoryForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, "सफलतापूर्वक कोटि थपियो")
            else:
                messages.success(request, "पोस्ट गर्न समस्या छ")

    return render(request, "manager/sub-category.html", dist)

def deleteSubCategory(request , id):
    cate = SubCategory.objects.get(id = id)
    cate.delete()
    messages.success(request, "तपाईंको कोटि मेटाइएको छ")
    return HttpResponseRedirect(reverse('manager:subcategory'))

def userList(request):
    latest = News.objects.all().order_by('-id')[:5]
    category = Category.objects.all().order_by('-id')[:8]
    form = UserForm()
    all_category = User.objects.all().order_by('-id')
    password_form = PasswordChangeFormUpdate(request.user)
    dist = {
        'category':category,
        'latest':latest,
        'form':form,
        'all_category':all_category,
        'password_form':password_form
    }
    if request.method == 'POST':
        try:
            User.objects.create_superuser(username = request.POST['username'], email = request.POST['email'], password=request.POST['password'])
            messages.success(request, "सफलतापूर्वक प्रयोगकर्ता थपियो")
        except:
            messages.success(request, "पोस्ट गर्न समस्या छ")

    return render(request, "manager/user.html", dist)

def deleteUser(request , id):
    cate = User.objects.get(id = id)
    cate.delete()
    messages.success(request, "तपाईंको प्रयोगकर्ता मेटाइएको छ")
    return HttpResponseRedirect(reverse('manager:userList'))

def nowLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage:homepage'))

def checkPassword(request):
   if request.method == 'POST':
        form = PasswordChangeFormUpdate(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'तपाईंको पासवर्ड सफलतापूर्वक अद्यावधिक गरियो')
            
        else:
            error = form.errors.as_data()
        
            messages.success(request, error)
       
        return HttpResponseRedirect(reverse('manager:userList'))