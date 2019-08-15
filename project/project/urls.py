"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import store.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',store.views.index, name="index"),
    path('store/',store.views.store, name="store"),
    path('search/',store.views.search, name="search"),
    path('wait/<int:store_id>/',store.views.wait, name="wait"),
    path('phone/', store.views.phone, name="phone"),
    path('clientnew/', store.views.clientnew, name="clientnew"),
    path('signup/', store.views.signup, name='signup'),
    path('login/', store.views.login, name='login'),
    path('logout/', store.views.logout, name='logout'),
    path('store/new/', store.views.new, name='new'),
    path('store/create/', store.views.create, name='create'),
    
]
