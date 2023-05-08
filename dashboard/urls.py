# from django.urls import path

from django.contrib import admin
from django.urls import include, path

from . import views

urlpatterns = [
   
   path('lpg', views.lpg, name='lpg'),
   path('website', views.website, name='website'),
   
   
   
    
   path('images', views.generate_image_from_text, name='images'),
   path('home', views.home, name='dashboard'),
   path('profile', views.profile, name='profile'),
   path('<str:ref_code>/', views.profile, name='profile'),
   
   path('delete-blog-topic/<str:uniqueId>/', views.deleteBlogTopic, name='delete-blog-topic'),
   path('generate-blog-from-topic/<str:uniqueId>/', views.createBlogFromTopic, name='generate-blog-from-topic'),
   
   
  
   #Blog Generation Routes 
   path('generate-blog-topic', views.blogTopic, name='blog-topic'),
   path('generate-blog-sections', views.blogSections, name='blog-sections'),
   
   #Saving the blog topic for future resue
   path('save-blog-topic/<str:blogTopic>/', views.saveBlogTopic, name='save-blog-topic'),
   
   path('use-blog-topic/<str:blogTopic>/', views.useBlogTopic, name='use-blog-topic'),
   path('view-generated-blog/<slug:slug>/', views.viewGeneratedBlog, name='view-generated-blog'),
   
  
  
   path('query', views.query, name='query'),
   path('translate', views.translate, name='translate'),
   path('ptranslate', views.P_translate, name='ptranslate'),
   
   path('generate-web-topic', views.webTopic, name='web-topic'),
   path('generate-web-sections', views.webSections, name='web-sections'),
   
   path('save-web-topic/<str:webTopic>/', views.saveWebTopic, name='save-web-topic'),
   path('use-web-topic/<str:webTopic>/', views.useWebTopic, name='use-web-topic'),
   path('view-generated-web/<slug:slug>/', views.viewGeneratedWeb, name='view-generated-web'),
   
   
   # path('delete-web-topic/<str:uniqueId>/', views.deleteWebTopic, name='delete-blog-topic'),
   path('generate-web-from-topic/<str:uniqueId>/', views.createWebFromTopic, name='generate-blog-from-topic'),
   
   # path('error-handler/', views.error_handler, name='error_handler'),
  
  
  
  
  
   path('billing', views.billing, name='billing'),
   path('534dac52-731d-439d-ac5f-773b29a9bfa4', views.webhook, name='webhook'),
   
   path('paypal-payment-success', views.PaypalPaymentSuccess, name='payment-success'),
   
   
   
   
   
   
]