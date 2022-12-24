from django.urls import path
from .import views


app_name = 'manager'

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('news', views.news, name = "news"),
    path('logout', views.nowLogout, name = "nowLogout"),
    path('allNews', views.allNews, name="allNews"),
    path('deleteNews/<int:id>', views.deleteNews, name = "deleteNews"),
    path('update-news/<int:id>', views.updateNews, name = "updateNews"),
    path('category', views.CategoryView, name = "category"),
    path('delete-category/<int:id>', views.deleteCategory, name = "deleteCategory"),
    path('sub-category', views.subCategoryView, name = "subcategory"),
    path('delete-sub-category/<int:id>', views.deleteSubCategory, name = "deleteSubCategory"),
    path('user-list', views.userList, name = "userList"),
    path('delete-user/<int:id>', views.deleteUser, name = "deleteUser"),
    path('check-password', views.checkPassword, name = "checkPassword"),
    path('news-selected/<str:str>', views.cnews, name = "cnews"),
]