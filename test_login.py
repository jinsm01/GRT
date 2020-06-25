from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin:
    def setup_method(self):
        self.driver = webdriver.Chrome()

    def teardown_method(self):
        self.driver.quit()

    def test_login(self):
        self.driver.get("http://www.tcc.edu.cn/")
        self.driver.set_window_size(1298, 782)
        self.driver.find_element(By.LINK_TEXT, "登录").click()
        self.driver.find_element(By.ID, "username").click()
        self.driver.find_element(By.ID, "username").send_keys("")
        self.driver.find_element(By.ID, "password").click()
        self.driver.find_element(By.ID, "password").send_keys("")
        self.driver.find_element(By.CSS_SELECTOR, "#btn_submit").click()
