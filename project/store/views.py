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
    store = Store.objects.get(pk=store_id)
    client = Client.objects.filter(store_id=store.id)
    context = {}
    context['store'] = store_detail
    context['client'] = client
    return render(request, 'wait.html', context)

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

def phone(request, store_id):
    phone_detail = get_object_or_404(Store, pk=store_id)
    print(store_id, 'store idddddddddddddd')
    return render(request, 'phone.html', {'phone': phone_detail})


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

def create_client(request, store_id):
    
    store = Store.objects.get(pk=store_id)
    
    
    store.num += 1
    store.recent_num += 1
    print(type(store),'storeeeeeeeee')
    mynum = store.recent_num
    phone_num = request.POST['phone']
    
    
    
    client = Client(store_id=store.id, phonenum=phone_num, my_num=mynum)
    client.save()
    store.save()

    context = {}
    context['store'] = store
    context['client'] = Client.objects.filter(store_id=store.id)
    print(len(context['client']), 'lennnnnnnnnnnnnnnnnn')
    return redirect('/wait/' + str(store.id))

# def confirm(request, client_id):
#     client = Client.objects.all()
#     phoneNum = request.POST['phone']
#     for c in client:
#         if phoneNum==c.phonenum:

# def cancel(request):
#     Client.objects.