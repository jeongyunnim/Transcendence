from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from .models import User

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')
    elif request.method =='POST':
        username = request.POST.get('username',None)
        useremail = request.POST.get('useremail',None) #새로 추가
        password = request.POST.get('password',None)
        re_password = request.POST.get('re-password',None)

        res_data ={}
        if not (username and useremail and password and re_password):
            res_data['error'] = '모든 값을 입력해야 합니다!'
        

        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다!'
        else:

            user = User(
                username=username,
                useremail=useremail, #새로 추가
                password = make_password(password)

            )
            user.save()
        return render(request, 'signup.html', res_data)