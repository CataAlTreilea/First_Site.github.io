from django.urls import path
from . import views

urlpatterns = [
path('', views.home, name='home'),
path('about', views.about, name='about'),
path('form', views.form, name='form'),
path('chatbot', views.chatbot, name='chatbot'),
path('gallery', views.gallery, name='gallery'),
]
