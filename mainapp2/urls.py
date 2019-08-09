from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('1//', views.send_sms,name='sms'),
    path('',views.home,name='home'),
    path('hello/',views.hello,name='hello'),
    path('waiting/',views.hello,name='waiting'),
    path('join/',views.join,name='join'),
]