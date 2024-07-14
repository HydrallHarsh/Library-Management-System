from django.contrib import admin
from django.urls import include, path

from Main import views

urlpatterns = [
    path('', views.mainScreen, name='Home'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('logout', views.logout, name='logout'),
    path('about_us', views.about_us, name='about_us'),
    path('profile', views.profile, name='profile'),
    path('settings', views.settings, name='settings'),
]
