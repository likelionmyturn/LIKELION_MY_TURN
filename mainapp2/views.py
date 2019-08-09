from django.shortcuts import render, get_object_or_404,redirect
from django.shortcuts import render
from django.http import HttpResponse
from sdk.api.message import Message
from sdk.exceptions import CoolsmsException
from .models import Number
from .form import PostForm

def send_sms(request):
    if request.method == 'POST':
        unum=Number()
        print("안녕하세용ㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇ")
        # set api key, api secret
        api_key = "NCSXPJSH89F75QH8"
        api_secret = "R6A4XNK2Z6OH8I1HTVDMIDAPRGGTXMPJ"

        unum.num=request.POST['usernum']
        unum.save()
        params = dict()
        params['type'] = 'sms' # Message type ( sms, lms, mms, ata )
        params['from'] = '01027629495' # Sender number
        params['to'] = unum.num
        params['text'] = '마이턴 테스트 문자입니다.1' # Message

        cool = Message(api_key, api_secret)
        try:
            response = cool.send(params)
            print("Success Count : %s" % response['success_count'])
            print("Error Count : %s" % response['error_count'])
            print("Group ID : %s" % response['group_id'])

            if "error_list" in response:
                print("Error List : %s" % response['error_list'])

        except CoolsmsException as e:
            print("Error Code : %s" % e.code)
            print("Error Message : %s" % e.msg)
        return render(request,'hello.html')
    return render(request,'hello.html')

def hello(request):
    return render(request,'hello.html')

def home(request):
    return render(request,'home.html')

def waiting(request):
    return render(request,'waiting.html')

def join(request):
    return render(request,'join.html')