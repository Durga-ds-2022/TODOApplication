"""TODO URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""
from django.urls import path
from home import views

urlpatterns = [
    path('', views.home, name='home'),
    path('update_todo/', views.update_todo, name='update_todo'),
    path('delete_todo/<int:id>/', views.delete_todo, name='delete_todo'),


]

