from django.urls import path
from .import views

app_name = "homepage"

urlpatterns= [
    path('', views.Homepage, name="homepage"),
    path('login', views.Login, name ="login"),
    path('news-details/<int:id>', views.newsDetails, name = "newsDetails")
]