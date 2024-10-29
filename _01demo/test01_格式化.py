def print_func(par):
    print("Hello : ", par)
    return


# 定义方法
def func2(par):
    print("Hello : ", par)
    return


# 调用方法
func2("1234")
func2("222")


print(f"f函数格式化：id={1}")
print("format格式化：id={}".format(1))


# 不换行输出‌：将end参数设置为空字符串''，可以使print函数在输出后不自动换行
print("不换行", end="")
print("内容")