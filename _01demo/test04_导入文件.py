
import sys

print('命令行参数如下:')
for i in sys.argv:
    print(i)

print('\n\nPython 路径为：', sys.path, '\n')

# 导入模块,一个文件就是一个模块
import support
# 现在可以调用模块里包含的函数了
support.print_func("w3cschool")
support.func2("aa")

# 导入指定函数
from support import func2
func2("a")

s = 'Hello, world.'

'-3.14'.zfill(7)
print('We are the {} who say "{}!"'.format('knights', 'Ni'))

print('This {name} is {age}.'.format(name='jim', age=12))

# 可选项 ':' 和格式标识符可以跟着字段名。 这就允许对值进行更好的格式化。
import math
print('The value of PI is approximately {0:.3f}.'.format(math.pi))

# 在 ':' 后传入一个整数, 可以保证该域至少有这么多的宽度。 用于美化表格时很有用。
table = {'Sjoerd': 1, 'Jack': 1234, 'Dcab': 12345678}

for name, phone in table.items():
 print('{0:10} ==> {1:10d}'.format(name, phone))




# 导入  operator 模块
import operator

# 初始化变量
a = 4

b = 3

# 使用 add() 让两个值相加
print(f"add() 运算结果:{operator.add(a, b)}")

# 使用 sub() 让两个值相减
# print("sub() 运算结果 :", end="");
print(operator.sub(a, b))

# 使用 mul() 让两个值相乘
# print("mul() 运算结果 :", end="");
print(operator.mul(a, b))

a = [1, 2]
b = [2, 3]
c = [2, 3]
print("operator.eq(a,b): ", operator.eq(a,b))
print("operator.eq(c,b): ", operator.eq(c,b))