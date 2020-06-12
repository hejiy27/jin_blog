from venv import logger

from django.contrib.auth import login
from django.http import HttpResponse
from django.shortcuts import render, redirect

from members.forms import RegisterForm
from members.models import User


def register(request):
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
        return render(request, 'registration/login.html',{'user':user})
    else :
        user_form = RegisterForm()
    return render(request,'registration/register.html', {'user_form':user_form})

def signup(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = User.objects.create_user(**form.cleaned_data)
            login(request, new_user)
            return redirect('main')
        else:
            return HttpResponse('사용자명이 이미 존재합니다.')
    else:
        form = RegisterForm()
        return render(request, 'registration/register.html', {'form': form})
        #return render(request, 'memo_app/adduser.html', {'form': form})


def main_page(request):
    return render(request,'blogs/base.html')

# def post_singles(request):

