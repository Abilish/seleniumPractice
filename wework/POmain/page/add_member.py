from time import sleep

from selenium.webdriver.common.by import By

from wework.POmain.page.base_page import BasePage


class Addmember(BasePage):

    def add_member(self):
        # send save

        self.find(By.ID, 'username').send_keys('malatang')
        self.find(By.ID, 'memberAdd_acctid').send_keys('321321')
        self.find(By.ID, 'memberAdd_phone').send_keys('32132132132')
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()

    def update_page(self):
        content:str = self.find(By.CSS_SELECTOR, '.ww_pageNav_info_text').text
        return [int(x) for x in content.split('/',1)]

    def get_member(self, value):
        self.wait_for_click((By.CSS_SELECTOR, '.ww_checkbox'))  # 按钮可被点击，最复杂，查找按钮，而不是查找文字
        cur_page, total_page = self.update_page()
        while True:
            elements = self.finds(By.CSS_SELECTOR, '#member_list>tr>td:nth-child(2)')
            for element in elements:
                if value == element.get_attribute("title"):
                    return True
            cur_page = self.update_page()[0]
            if cur_page == total_page:
                return False
            self.find(By.CSS_SELECTOR, '.js_next_page').click()

        # return [element.get_attribute('title') for element in elements]
        # for element in elements:
        #     list.append(element.get_attribute('title'))


