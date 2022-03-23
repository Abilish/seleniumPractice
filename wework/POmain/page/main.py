from time import sleep
from selenium.webdriver.common.by import By
from wework.POmain.page.add_member import Addmember
from wework.POmain.page.base_page import BasePage


class Main(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame'
    def goto_add_member(self):
        # click
        sleep(2)
        self.find(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        return Addmember(self._driver)
