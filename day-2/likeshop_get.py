"""
1. 请求likeshop项目的登录接口，URL： http://liketest.com/api/cart/lists
2. 请求头： Content-Type: application/json
3. 请求体： {"mobile":"13800000002", "password":"123456"}
"""

import requests

# 发送登录请求
login_url = "http://liketest.com/api/account/login"
login_data =  {
     "account":"17681879698",
     "password":"admin123456",
     "client":6
 }
response = requests.post(url=login_url, json=login_data)
print(response.json())
token=response.json().get("data").get("token")
# print(response.json().get("data").get("token"))


cart_list_url = "http://liketest.com/api/cart/lists"

stringA = ""
login_header = {
    "Content-Type": "application/json",
    "token":token
}
# 发送请求
response = requests.get(url=cart_list_url, params=stringA,headers=login_header)

# 查看响应
print(response.json())