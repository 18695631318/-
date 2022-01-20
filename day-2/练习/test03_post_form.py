"""
1. 请求TPshop项目的登录接口，
请求数据（username: 17681879698, password: 123456, verify_code: 6666）
2. 登录接口URL：http://tpshop.com/index.php?m=Home&c=User&a=do_login
"""

# 导包
import requests

# 发请求
# url = "http://tpshop.com/index.php?m=Home&c=User&a=do_login"
# data = {
#     "username": "17681879698",
#     "password": "123456",
#     "verify_code": "6666"
# }
# response = requests.post(url, data)
#
# # 看响应
# print(response.json())



url2 = "http://liketest.com/api/cart/lists"
#
# response = requests.get(url2)

#  （2）字典
dictA = {
    "keyword": "手机"
}
response = requests.get(url2, dictA)
# 查看响应
print(response.json())