# 定义函数, 以：结尾
# 形参默认值
def test1(name='一', age=10):
    str1: str = f"姓名={name},年龄(默认值10)={age}"
    print(str1)
    return str1


test1("tom", 3)
test1("jim")

# 指定参数名称
test1(name="lili")
test1(name='jack', age=20)
# 参数有默认值，就可以随便传参，没有默认值，不传报错
test1(age=20)
