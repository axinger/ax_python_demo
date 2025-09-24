def my_decorator(func):
    def AA(*args, **kwargs):  # 修改为接受任意参数
        print("在调用函数之前，会发生一些事情", args, kwargs)
        res = func(*args, **kwargs)  # 将参数传递给原函数
        print("在调用函数之后，会发生一些事情=", res, args, kwargs)
        return res  # 返回原函数的结果,不然会返回None

    return AA


@my_decorator
def say_hello(name):
    print("你好,", name)
    return "1234"


if __name__ == '__main__':
    res = say_hello('tom')
    print('调用结果=', res)
