from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', practice, name='practice'),
    path('conversation/<int:pk>', showConversation, name='newPractice'),
   
]
