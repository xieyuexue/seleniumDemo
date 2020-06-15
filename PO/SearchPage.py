# coding=utf-8
__author__ = 'xieyuexue'
from selenium import webdriver
from selenium.webdriver.common.by import By
from .BasePage import Base


class Dash(Base):
    # 登录按钮
    login = (By.CLASS_NAME, 'noUser')
    # 手机号输入框
    phone_input = (By.XPATH, '//*[@id="__layout"]/div/div/div[2]/div/div/form/div[1]/div/div[2]/input')
    # 密码输入框
    pwd_input = (By.XPATH, '//*[@id="__layout"]/div/div/div[2]/div/div/form/div[2]/div/input')
    # 登录按钮
    login_button = (By.CLASS_NAME, 'loginhBtn')

    # 搜索输入框
    search_loc = (By.TAG_NAME, "input")
    # 搜索按钮
    input_loc = (By.CLASS_NAME, "searchBtn")

    # 输入手机号
    def input_phone(self, phone_input):
        self.send_keys(self.phone_input, phone_input)

    # 输入密码
    def input_pwd(self, pwd_input):
        self.send_keys(self.pwd_input, pwd_input)

    # 点击登录按钮
    def click_login_button(self, login_button):
        self.clickButton(self.login_button)

    # 输入搜索关键词
    def input_recipe(self, search_loc):
        self.send_keys(self.search_loc, search_loc)

    # 定位点击搜索框，进入搜索页面
    def click_search_box(self):
        self.clickButton(self.input_loc)
