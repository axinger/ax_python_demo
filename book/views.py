from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

# 第一个参数，固定 request
def book_str(request):
    id = request.GET.get("id")  # get请求获取参数

    # resolve("index") # 请求翻转，请求转发
    return HttpResponse(f"get请求获取参数{id}")


def book_str2(request, id):
    return HttpResponse(f"get请求获取参数={id}")


def book_str3(request, id):
    return HttpResponse(f"get请求获取参数={id}")


def index(request):
    return render(request, "index.html")
