# 导入 requests 包
import requests

# 发送请求
x = requests.request('get', 'https://www.w3cschool.cn/')

# 返回网页内容
print(x)