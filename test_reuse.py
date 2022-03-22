from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


# 1. 需要安装selenium库，并导入
# 2. 需要安装pytest，并在设置中将 "Default test runner" 改为 pytest
# 3. 更改配置，创建（选择）pytest配置项。选择项目、命名

class TestReuse():
    def setup_method(self, method):
        # options = Options()
        # options.debugger_address = '127.0.0.1:9222'
        # self.driver = webdriver.Chrome(options=options)
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_reuse(self):
        self.driver.get("https://cn.bing.com/?ensearch=1&FORM=BEHPTB")  # 复用时可以注释掉该页面
        self.driver.find_element(By.ID, "est_cn").click()
        sleep(3)
