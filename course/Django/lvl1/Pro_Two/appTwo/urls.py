from django.urls import path
from django.urls import re_path
from appTwo import views

urlpatterns = [
    path('help', views.help, name='help'),
    path('first', views.page1, name='page1'),
    path('second', views.page2, name='page2')
]
