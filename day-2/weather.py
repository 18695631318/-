import requests
#
# # 1). 访问查询天气信息的接口，并获取JSON响应数据
# # 2). 接口地址：http://www.weather.com.cn/data/sk/101010100.html
response = requests.get("http://www.weather.com.cn/data/sk/101010100.html")
print(response.json())
