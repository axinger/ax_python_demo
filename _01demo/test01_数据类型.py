import datetime

print(f'当前时间{datetime.datetime.now()}')
print(f'当前时间{datetime.timedelta(days=1)}')
print(f'当前时间{datetime.datetime.now() - datetime.timedelta(days=1)}')
print(f'当前时间{datetime.datetime.now() + datetime.timedelta(days=1)}')
print(f'当前时间{datetime.datetime.now().day-1}')

age: int = 1
print(age)

# 类型不强校验
age = 'a'
print(age)
