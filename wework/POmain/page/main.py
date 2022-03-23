from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from wework.POmain.page.add_member import Addmember
from wework.POmain.page.base_page import BasePage


class Main(BasePage):
    _base_url = 'https://work.weixin.qq.com/wework_admin/frame'
    def goto_add_member(self):
        # click
        def wait_add_member(x):
            elements_len = len(self.finds(By.CSS_SELECTOR, '#username'))
            if elements_len <= 0:
                self.find(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)')
            return elements_len > 0
        self.wait_for_element(wait_add_member)

        # locator = (By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)')
        # self.wait_for_click(locator, 10)

        # self.find(By.CSS_SELECTOR, '.index_service_cnt_itemWrap:nth-child(1)').click()
        return Addmember(self._driver)
