# from django.urls import path

from django.urls import path,include


from . import views

urlpatterns = [
   path('login/', views.login, name='login/'),
   path('register', views.register, name='register'),
  path("logout", views.logout, name="logout"),
  path("", include('django.contrib.auth.urls')),
  
 
]