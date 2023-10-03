from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('messages/',messagesFunc,name='messages'),
    path('delMsg/<id>/',delMsg,name='delMsg'),
    path('viewMsg/<id>/',viewMsg,name='viewMsg'),
]
