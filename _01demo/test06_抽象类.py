from abc import ABC, abstractmethod


# 定义抽象类
class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass  #pass 是一个占位符语句，表示"什么也不做"

    @abstractmethod
    def move(self):
        pass


# 派生类实现抽象方法
class Dog(Animal):
    def sound(self):
        pass

    # def sound(self):
    #     print("Bark")

    def move(self):
        print("Run")


# 不能直接实例化抽象类
# animal = Animal()  # TypeError: Can't instantiate abstract class Animal with abstract methods sound, move

# 实例化派生类
dog = Dog()
dog.sound()  # 输出: Bark
dog.move()  # 输出: Run

x = 10

if x > 5:
    pass
else:
    print("x is 5 or less")
