
class People:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问,两个下划线开头，声明该属性为私有
    __weight = 0

    # 定义构造方法
    def __init__(self, n, age, w):
        self.name = n
        self.age = age
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))

    def fun(self,age):
        print("%s 说: 我 %d 岁。" % (self.name, self.age),age)
# 实例化类
p = People('W3Cschool',10,30)
p.speak()
p.fun(1111)



#单继承示例
class Student(People):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构函
        People.__init__(self,n,a,w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))

# Python 同样有限的支持多继承形式。
# 若是父类中有相同的方法名，而在子类使用时未指定，Python 从左至右搜索 即方法在子类中未找到时，从左到右查找父类中是否包含方法


'''
类的专有方法：

    __init__ : 构造函数，在生成对象时调用
    __del__ : 析构函数，释放对象时使用
    __repr__ : 打印，转换
    __setitem__ : 按照索引赋值
    __getitem__: 按照索引获取值
    __len__: 获得长度
    __cmp__: 比较运算
    __call__: 函数调用
    __add__: 加运算
    __sub__: 减运算
    __mul__: 乘运算
    __div__: 除运算
    __mod__: 求余运算
    __pow__: 乘方
'''
