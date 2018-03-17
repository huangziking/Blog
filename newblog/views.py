from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Post
def index(request):
    return render(request,'newblog/index.html',context={
        'title':'我的首页',
        'welcome':'欢迎访问的的首页'
    })
def detail(request,pk):
    post = get_object_or_404(Post,pk=pk)
    return render(request,'newblog/detail.html',context={'post':post})