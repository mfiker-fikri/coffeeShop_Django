from django.urls import path
from . import views

urlpatterns = [
    # 
    path('', views.homes, name='indexs'),
    # 
    path('about/', views.abouts, name='abouts')
]