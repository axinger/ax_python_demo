from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from book.forms import BookForm
from book.models import SysUser


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
    return render(request, "index.html",
                  context={
                      "name": "jim"
                  })


def addSysUser(request):
    # 在Django的模型中使用.objects.create(),不需要显式调用save()
    # SysUser.objects.create(name="tom",age=10)
    user = SysUser(name="jim", age=10)
    user.save()
    return HttpResponse(f"插入数据库={user}")


@require_http_methods(["GET"])  # 指定请求方式
def getSysUser(request):
    # 查询所有
    for e in SysUser.objects.all():
        print(e.id)

    # 过滤,
    # user = SysUser.objects.filter(name="jim").get(id=1)

    # get 没有满足条件的，会抛出异常
    user = SysUser.objects.get(id=1)

    list = SysUser.objects.order_by("-createTime")

    for e in list:
        print(e.id)

    return HttpResponse(f"查询数据库={user},{list}")


def deleteSysUser(request):
    user = SysUser.objects.get(id=1).delete()
    return HttpResponse(f"删除数据库={user}")


def updateSysUser(request):
    user = SysUser.objects.get(id=1)
    user.age = 20
    user.save()
    return HttpResponse(f"更新数据库={user}")


# Q表达式
def getSysUserQ(request):
    # &  |
    user = SysUser.objects.filter(Q(name__contains='j') & Q(age__gt=2)).all()

    return HttpResponse(f"更新数据库={user}")


@require_http_methods(["POST"])  # 指定请求方式
def getFormUser(request):
    form = BookForm(request.POST)
    if form.is_valid():

        # form.title
        title = form.cleaned_data.get("title")
        return HttpResponse(f"表单验证成功title={title}")

    else:
        return HttpResponse(f"表单验证失败")
