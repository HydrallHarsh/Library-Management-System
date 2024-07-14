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
    path('add_book',views.add_book,name='add_book'),
    path('remove_book/', views.remove_book, name='remove_book'),
    path('confirm_remove_book/<str:isbn_13>/', views.confirm_remove_book, name='confirm_remove_book'),
     path('add-to-cart/<str:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('view-cart/', views.view_cart, name='view_cart'),
    path('settings', views.settings, name='settings'),
    # path('transactions', views.transactions, name='transactions'),
]
