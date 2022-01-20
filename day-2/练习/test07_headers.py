"""
1. 请求likeshop项目的登录接口，URL： http://ihrm-test.itheima.net/api/sys/login
2. 请求头： Content-Type: application/json
3. 请求体： {"mobile":"13800000002", "password":"123456"}
"""

import requests
login_url = "http://ihrm-test.itheima.net/api/sys/login"
login_header = {
    "Content-Type": "application/json"
}
login_data ={
    "mobile": "13800000002",
    "password": "123456"
}
# 发送请求
response = requests.post(url=login_url, json=login_data, headers=login_header)

# 查看响应
print(response.json())


# 发送登录请求
login_url = "http://liketest.com/api/account/login"
login_data =  {
     "account":"17681879698",
     "password":"admin123456",
     "client":6
 }

response = requests.post(url=login_url, json=login_data)
# print(response.json())
token=response.json().get("data").get("token")

header={
    "token":token
}
# print(token)
order_url="http://liketest.com/api/order/lists"
data2={
    "type":"all"
}
response2 = requests.get(url=order_url,params=data2,headers=header)
print(response2.json())
