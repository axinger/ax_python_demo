def my_decorator(func):
    def wrapper():
        print("在调用函数之前，会发生一些事情。")
        func()
        print("在调用函数之后，会发生一些事情。")

    return wrapper


@my_decorator
def say_hello():
    print("你好！")


say_hello()

import django

print(django.get_version())
