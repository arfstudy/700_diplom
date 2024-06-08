"""
URL configuration for users application.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
"""
from django.urls import path
from rest_framework.routers import DefaultRouter

from backend import views

app_name = 'backend'

router = DefaultRouter()
router.register(prefix='contact', viewset=views.ContactModelView, basename='contact')

urlpatterns = [
    # Работает с контактом пользователя.                http://127.0.0.1:8000/api/v1/backend/contact/
] + router.urls
