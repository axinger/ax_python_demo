from math import trunc
from sys import excepthook

print("我的11111111")

# 查询所有关键字
'''
多行注释
'''
import keyword

print(keyword.kwlist)

name ="jim"
print(type(name))

str = 'W3Cschool'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始后的所有字符
print(str[1:5:2])  # 输出从第二个开始到第五个且每隔两个的字符
print(str * 2)  # 输出字符串两次
print(str + '你好')  # 连接字符串

print('------------------------------')

print('hello\nW3Cschool')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nW3Cschool')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义


# x=input("请输入X的值：") # 这是一个常见的input样例，他输出提示信息，然后接受一个字符串并将值传递给一个变量X
# print(x) # 打印变量，可以看到输入的x的值
# print(type(x)) #查看这个变量的类型


isName = True
print(isName)

# 一个变量可以通过赋值指向不同类型的对象。
a,b = 1,1.2
print(a)
print(b)
print(type(b))
b=1
print(type(b))

print(2 / 4  )# 除法，得到一个浮点数
print(2 // 4 )# 除法，得到一个整数
print(2 ** 5) # 乘方

word = 'Python'
print(word[0], word[5])
print(word[-6],word[-1] )


word = 'ilovepython'
print(word[1:5])


a = ['him', 25, 100, 'her']
print(a)

a = [1, 2, 3, 4, 5]
a=a + [6, 7, 8]
print(a)

a[2:7] = [13, 14, 15] # 【2,7）替换为后面的内容
print(a)

# 元组（tuple）与列表类似，不同之处在于元组的元素不能修改。元组写在小括号里，元素之间用逗号隔开。

a = (1991, 2014, 'physics', 'math')
print(a, type(a), len(a))

tup1 = () # 空元组
tup2 = (20,) # 一个元素，需要在元素后添加逗号
print(type(tup2))

# Sets（集合）
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)   # 重复的元素被自动去掉


tel = {'Jack':1557, 'Tom':1320, 'Rose':1886}
print(tel['Jack'] )  # 主要的操作：通过key查询
del tel['Rose']  # 删除一个键值对
tel['Mary'] = 4127  # 添加一个键值对
list(tel.keys())  # 返回所有key组成的list
print("所有的key，并排序：",sorted(tel.keys()) )# 按key排序
print('Tom' in tel     )  # 判断是否存在
print('Tom' not in tel     )  # 判断是否存在

print(tel.keys())
print(tel.values())
tel.clear()
print(tel)

a = 21
b = 10
c = 0

if a == b:
    print ("a 等于 b")
else:
    print ("a 不等于 b")

list1=[1,2,3,4]
for e in list1:
    print(e)


a = [66.25, 333, 333, 1, 1234.5,'a']
print(a.count(333), a.count(66.25), a.count('x')) # 返回 x 在列表中出现的次数。



