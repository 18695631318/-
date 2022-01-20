#获取验证码
import requests
session=requests.Session();
response=session.get("http://tpshop.com/index.php?m=Home&c=User&a=verify")
print(response.cookies)