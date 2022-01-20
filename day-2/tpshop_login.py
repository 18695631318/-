"""
1. 使用requests库调用TPshop登录功能的相关接口，完成登录操作
2. 登录成功后获取‘我的订单’页面的数据
接口地址：
获取验证码：http://localhost/index.php?m=Home&c=User&a=verify
登录用户：（username: 17681879698, password: 123456, verify_code: 1234）
登录：http://localhost/index.php?m=Home&c=User&a=do_login
我的订单：http://localhost/Home/Order/order_list.html
"""
import requests
# 获取验证码
# response = requests.get("http://tpshop.com/index.php?m=Home&c=User&a=verify")
# print(response.cookies)
# PHPSESSID = response.cookies.get("PHPSESSID")
# print(PHPSESSID)
# 登录
# login_url = "http://tpshop.com/index.php?m=Home&c=User&a=do_login"
# login_data = {"username": "17681879698", "password": "123456", "verify_code": "6666" }
# cookies = { "PHPSESSID": PHPSESSID }
# response = requests.post(url=login_url, data=login_data, cookies=cookies)
# print(response.json())
# # 我的订单：http://localhost/Home/Order/order_list.html
# response = requests.get("http://tpshop.com/Home/Order/order_list.html", cookies=cookies)
# print(response.text)


import requests
# 创建session对象
session = requests.Session()
# 获取验证码
response = session.get("http://tpshop.com/index.php?m=Home&c=User&a=verify")

# 登录
login_url = "http://tpshop.com/index.php?m=Home&c=User&a=do_login"
login_data = { "username": "17681879698", "password": "123456", "verify_code": "6666" }
response = session.post(url=login_url, data=login_data)
print(response.json())
# 我的订单：http://tpshop.com/Home/Order/order_list.html
response = session.get("http://tpshop.com/Home/Order/order_list.html")
print(response.text)