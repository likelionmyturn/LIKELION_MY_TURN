from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Store
from django.http import HttpResponseNotFound

# Create your views here.

def index(request):
    return render(request,'index.html')

def main(request):
    return render(request,'main.html')

def wait(request):
    return render(request,'wait.html')

def store(request):
    stores = Store.objects
    store_list = Store.objects.all()
    paginator = Paginator(store_list, 5)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
        page = 1
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'home.html', {'posts': posts, 'pages': range(1, paginator.num_pages+1), 'current': int(page), 'user': request.user })


def search(request):
    if request.method == 'POST':
        storeList = Store.objects.filter(body__icontains=request.POST['search'])
        print(storeList)
        return render(request,'search.html',{'posts':storeList,'user':request.user })
    else:
        return HttpResponseNotFound("없는 페이지 입니다.")

def phone(request):
    return render(request, 'phone.html')