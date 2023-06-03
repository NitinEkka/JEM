from django.contrib import admin
from django.urls import path
from jemapp import views

urlpatterns = [
    path('', views.homePage),
    path('mail/', views.mailView),
]