from django.urls import path
from .import views

app_name = "homepage"

urlpatterns= [
    path('', views.Homepage, name="homepage"),
    path('news-details/<int:id>/<slug:slug>', views.newsDetails, name = "newsDetails")
]