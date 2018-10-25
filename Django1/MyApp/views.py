from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# use this to response the data

def index(request):
    return HttpResponse('Deng Luo is very cool')


def detail(request, num):

    return HttpResponse("detail-%s"%num)
