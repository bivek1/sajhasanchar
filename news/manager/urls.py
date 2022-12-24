from django.urls import path
from .import views


app_name = 'manager'

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('news', views.news, name = "news"),
    path('logout', views.nowLogout, name = "nowLogout")
]