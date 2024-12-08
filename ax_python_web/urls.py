"""
URL configuration for ax_python_web project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('book', book_views.book_str, name='book'),  # name 路由翻转
    # # 定义restful 格式，定义类型
    # path('book/<str:id>', book_views.book_str2),
    # path('book/slug/<slug:id>', book_views.book_str3),  #
    # path('book/path/<slug:id>', book_views.book_str3),  # /1/2 为一个字符串

    path('', include('book.urls')), # include 方式，分层

    # path('head/', include('book.urls')),  # 统一path
]
