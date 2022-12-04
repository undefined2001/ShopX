from django.urls import path
from . import views


urlpatterns = [
   path('', views.store, name = "store"),
   path('register/', views.register, name = "register"),
   path('login/', views.user_login, name = "login"),
   path('logout/', views.user_logout, name = "logout"),
   path('search/', views.search, name = "search"),
   path('product_details/', views.product_details, name = "product_details"),
]
