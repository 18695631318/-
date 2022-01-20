"""
1. 请求likeshop项目的登录接口，请求数据（ {
     "account":"17681879698",
     "password":"admin123456",
     "client":6
 }）
2. 登录接口URL：http://liketest.com/api/account/login
"""
# 导包
import requests

# 发送登录请求
login_url = "http://liketest.com/api/account/login"
login_data =  {
     "account":"17681879698",
     "password":"admin123456",
     "client":6
 }
response = requests.post(url=login_url, json=login_data)
respJson=response.json() #把结果转换成json数据
token=respJson['data']['token']
# # 查看响应
# print(resp_dict['data']['token'])
print(token)

# 发送登录请求
login_url = "http://liketest.com/api/account/login"
login_data =  {
     "account":"17681879698",
     "password":"admin123456",
     "client":6
 }
response = requests.post(url=login_url, json=login_data)

# 查看响应
print(response.json())
# 对结果进行断言
