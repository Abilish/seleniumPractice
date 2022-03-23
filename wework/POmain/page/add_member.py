from time import sleep

from selenium.webdriver.common.by import By

from wework.POmain.page.base_page import BasePage


class Addmember(BasePage):

    def add_member(self):
        # send save
        sleep(2)
        self.find(By.ID, 'username').send_keys('malatang')
        self.find(By.ID, 'memberAdd_acctid').send_keys('321321')
        self.find(By.ID, 'memberAdd_phone').send_keys('32132132132')
        self.find(By.CSS_SELECTOR, '.js_btn_save').click()
        sleep(2)

        return True

    def get_member(self):
        elements = self.finds(By.CSS_SELECTOR, '#member_list>tr>td:nth-child(2)')
        return [element.get_attribute('title') for element in elements]
        # for element in elements:
        #     list.append(element.get_attribute('title'))


