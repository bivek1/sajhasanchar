from django.urls import path
from .import views

app_name = "homepage"

urlpatterns= [
    path('', views.Homepage, name="homepage"),
    path('login', views.Login, name ="login"),
    path('news-details/<int:id>', views.newsDetails, name = "newsDetails"),
    path('news/<str:str>', views.selectNews, name = "selectNews"),
    path('category/<int:id>/<slug:slug>', views.categoryNews, name = "categoryNews")
]