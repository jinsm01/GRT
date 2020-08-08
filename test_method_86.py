#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 11:48
# @Author  : shaonianlang
# @File    : test_method_86.py

from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestAddStudent:
    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)   # //*[@href='#user']
        self.driver.get("http://pre.xuanxue.100cdw.com/console/5000")

    def teardown(self):
        sleep(3)
        self.driver.quit()

    def test_method(self):
        self.driver.find_element(By.ID, 'username').send_keys("china")
        self.driver.find_element(By.ID, 'password').send_keys("Zz123456")
        self.driver.find_element(By.ID, 'btn_submit').click()
        sleep(3)
        self.driver.refresh()
        sleep(3)
        self.driver.back()
        sleep(3)
        self.driver.find_element(By.ID, 'username').clear()
        print(self.driver.title)

    def test_login(self):
        self.driver.find_element(By.ID, 'username').send_keys("china")
        self.driver.find_element(By.ID, 'password').send_keys("Zz123456")
        self.driver.find_element(By.ID, 'btn_submit').click()

    def test_wait(self):
        self.test_login()
        self.driver.find_elements(By.XPATH, "//*[@class='btn btn-primary pull-right']")[0].click()
        self.driver.find_element(By.XPATH, "//*[@href='#user']").click()
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.ID, 'addNew')))
        self.driver.find_element(By.ID, 'addNew').click()

    def test_action_chains(self):
        self.test_login()
        personal = self.driver.find_element(By.CLASS_NAME, 'dropdown-toggle')
        ActionChains(self.driver).move_to_element(personal).perform()
        sleep(3)
        self.driver.find_element(By.ID, 'logoutLink').click()

    def test_double_click(self):
        self.test_login()
        self.driver.find_elements(By.XPATH, "//*[@class='btn btn-primary pull-right']")[0].click()
        # WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "//*[@href='#user']")))
        self.driver.find_element(By.XPATH, "//*[@href='#user']").click()
        sleep(3)
        countrywide = self.driver.find_element(By.XPATH, "//*[@class='ztree no-padding']/li/a")
        action = ActionChains(self.driver)
        action.double_click(countrywide)
        action.perform()

    def test_key_down_up(self):
        self.test_login()
        self.driver.find_elements(By.XPATH, "//*[@class='btn btn-primary pull-right']")[0].click()
        self.driver.find_element(By.XPATH, "//*[@href='#user']").click()
        sleep(3)
        input_name = self.driver.find_element(By.XPATH, "//*[@class='form-control']")
        ActionChains(self.driver).click(input_name).perform()
        ActionChains(self.driver).key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
        input_name.send_keys("test")

    def test_send_key(self):
        self.test_login()
        self.driver.find_elements(By.XPATH, "//*[@class='btn btn-primary pull-right']")[0].click()
        self.driver.find_element(By.XPATH, "//*[@href='#user']").click()
        sleep(3)
        input_name = self.driver.find_element(By.XPATH, "//*[@class='form-control']")
        ActionChains(self.driver).click(input_name).perform()
        ActionChains(self.driver).send_keys(Keys.SPACE).perform()
        input_name.send_keys("test")

    def test_copy(self):
        self.test_login()
        self.driver.find_elements(By.XPATH, "//*[@class='btn btn-primary pull-right']")[0].click()
        self.driver.find_element(By.XPATH, "//*[@href='#user']").click()
        sleep(3)
        input_name = self.driver.find_element(By.XPATH, "//*[@class='form-control']")
        ActionChains(self.driver).click(input_name).perform()
        ActionChains(self.driver).send_keys(Keys.SPACE).perform()
        input_name.send_keys("test")
        sleep(3)
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        sleep(3)
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('x').key_up(Keys.CONTROL).perform()
        sleep(3)
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

