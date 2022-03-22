import shelve
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class TestCookie():
    def setup_method(self, method):
        # options = Options()
        # options.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_cookie(self):
        cookies = [
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwruuutx.cs_ind', 'path': '/', 'secure': False,
             'value': ''},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwruuutx.cs_ind', 'path': '/',
             'secure': False,
             'value': ''},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwruuutx.cs_ind', 'path': '/',
             'secure': False,
             'value': ''},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwruuutx.cs_ind', 'path': '/',
             'secure': False,
             'value': ''},
            {'domain': '.work.weixin.qq.com', 'httpOnly': False, 'name': 'wwruuutx.cs_ind', 'path': '/',
             'secure': False,
             'value': ''}
            # cookie还有很多行已删，请自行登录获取
            ]

        # print(self.driver.get_cookies())
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame')
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        sleep(3)
