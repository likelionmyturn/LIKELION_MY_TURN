from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Store, Client
from django.http import HttpResponseNotFound
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.

def index(request):
    return render(request,'index.html')

def main(request):
    return render(request,'main.html')

def wait(request, store_id):
    store_detail = get_object_or_404(Store, pk=store_id)
    clients =  Client.objects
    clientph = Client.objects.values('phonenum')
    aa=0
    for i in clientph.values():
        aa+=1
        i

 
    return render(request, 'wait.html', {'store': store_detail,'clients':clients,'num':i,'aa':aa,'clientph':clientph})



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

def clientnew(request):
    client = Client()
    client.phonenum = request.POST['phonenum']
    client.save()

    return redirect('/store')


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(
                request.POST['username'], password=request.POST['password1'])
            auth.login(request, user)
            return redirect('store')
    return render(request, 'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('store')
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('store')
    return render(request, 'accounts/signup.html')

def new(request):
    return render(request, 'new.html')

def create(request):
    sto = Store()
    sto.title = request.GET['storename']
    sto.body = request.GET['location']
    sto.time = request.GET['cookingtime']
    sto.author = request.user
    sto.pup_date = timezone.datetime.now()
    sto.save()
    return redirect('/store/')
