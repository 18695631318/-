# 导包
import requests

# 发送请求
# 直接通过url传递参数
# response = requests.get(" http://tpshop.com/Home/Goods/search.html?q=iphone")

#  通过params传递参数：
#  （1）字符串
url = "http://tpshop.com/Home/Goods/search.html"
stringA = "q=iphone&a=d"
# response = requests.get(url=urlA, params=stringA)
response = requests.get(url, stringA)
#  （2）字典
avb = {
    "q": "手机"
}
response = requests.get(url, avb)
# # 查看响应
print(response)


urlA = "http://liketest.com/api/goods/getGoodsList"
stringA = "keyword=手机"
response = requests.get(url=urlA, params=stringA,)

#  （2）字典
dictA = {
    "keyword": "手机"
}
response = requests.get(url=urlA, params=dictA)
# 查看响应
print(response.json())