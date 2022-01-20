# 获取验证码： http://tpshop.com/index.php?m=Home&c=User&a=verify
# 登录     ： http://tpshop.com/index.php?m=Home&c=User&a=do_login

# 导包
import requests
import unittest


# 创建测试类
class LikeShopLogin(unittest.TestCase):
    def setUp(self):
        # 实例化session对象
        self.session = requests.Session()
        # 定义验证接口url地址
        self.url_verify = "http://tpshop.com/index.php?m=Home&c=User&a=verify"
        # 定义正如接口url地址
        self.url_login = "http://liketest.com/api/account/login"

    # teardown
    def tearDown(self):
        # 关闭session对象
        self.session.close()

    # 登录成功
    def test01_login_success(self):

        # 发登录请求并断言
        login_data = {
            "account": "17681879698",
            "password": "admin123456",
             "client":6
        }
        response = self.session.post(url=self.url_login, data=login_data)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(1, response.json().get("code"))
        self.assertIn("登录成功", response.json().get("msg"))

    # 账号不存在
    def test02_user_is_not_exit(self):
        # 发登录请求并断言
        login_data = {
            "account": "17781879698",
            "password": "admin123456",
            "client": 6
        }
        response = self.session.post(url=self.url_login, data=login_data)
        print(response.json())
        self.assertEqual(200, response.status_code)
        self.assertEqual(0, response.json().get("code"))
        self.assertIn("账号不存在", response.json().get("msg"))

if __name__ == '__main__':
   # 启动单元测试
    unittest.main()
    # 获取TestSuite的实例对象
    suite = unittest.TestSuite()
