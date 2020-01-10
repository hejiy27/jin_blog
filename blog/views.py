from django.http import HttpResponse
from django.shortcuts import render



def hello(request):
    return HttpResponse("<h1>Response 보내기</h2?")