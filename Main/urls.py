from django.contrib import admin
from django.urls import include, path

from Main import views

urlpatterns = [
    path('', views.mainScreen, name='Home'),
]
