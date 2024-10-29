from django.urls import path

# from . 当前目录
from . import views as book_views

# 指定应用名称，命名空间
app_name = 'book'

urlpatterns = [
    path('book_index', book_views.index),  # name 路由翻转
    path('book', book_views.book_str, name='book_list'),  # name 路由翻转
    # 定义restful 格式，定义类型
    path('book/<str:id>', book_views.book_str2),
    path('book/slug/<slug:id>', book_views.book_str3),  #
    path('book/path/<slug:id>', book_views.book_str3),  # /1/2 为一个字符串
]
