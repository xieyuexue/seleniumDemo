# coding=utf-8
__author__ = 'xieyuexue'
from selenium import webdriver
from selenium.webdriver.common.by import By
from .BasePage import Base

class Login(Base):
    #登录按钮
    login = (By.CLASS_NAME,'noUser')
    #手机号输入框
    phone_input = (By.XPATH,'//*[@id="__layout"]/div/div/div[2]/div/div/form/div[1]/div/div[2]/input')
    #密码输入框
    pwd_input = (By.XPATH,'//*[@id="__layout"]/div/div/div[2]/div/div/form/div[2]/div/input')
    #登录按钮
    login_button = (By.CLASS_NAME,'loginhBtn')

    #输入手机号
    def input_phone(self,phone_num):
        self.send_keys(self.phone_input,phone_num)
    #输入密码
    def input_pwd(self,pwd):
        self.send_keys(self.pwd_input,pwd)
    #点击登录按钮
    def click_login_button(self):
        self.clickButton(self.login_button)