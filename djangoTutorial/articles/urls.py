from django.contrib import admin
from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('create/', views.article_create, name="create"),
    path('<slug>/', views.article_detail, name="detail"),
    path('', views.article_list, name="list")
]
