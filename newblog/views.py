from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'newblog/index.html',context={
        'title':'我的首页',
        'welcome':'欢迎访问的的首页'
    })