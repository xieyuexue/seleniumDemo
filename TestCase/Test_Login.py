# -*- coding: utf-8 -*-
__author__ = 'xieyuexue'
import unittest
from PO import LoginPage
from selenium import webdriver
from Public import Common
import time
class Search(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = Common.login_url()
        self.phone_num_right = '15662703754'
        self.phone_num_wrong = '15662700000'
        self.password_right = 'l12345678'
        self.password_wrong = '88888888'

    def test_Login_01(self):
        u'''UI-01
            前提条件：手机号已经被注册
            测试步骤：不输入账号，输入密码，点击登录
        '''
        print ("------只输入密码测试------")
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)

        login_page = LoginPage.Login(self.driver)
        login_page.input_pwd(self.password_right)
        login_page.click_login_button()

        #result = self.driver.find_element_by_class_name('UserErrorTips').text
        result  =self.driver.find_element_by_class_name('UserErrorTips').text.split()[0]
        print(result)
        except_result = u'请输入手机号码'
        self.assertEqual(result,except_result,msg="%s等于%s"%(result,except_result))

    def test_Login_02(self):
        u'''UI-02
            前提条件：手机号已经被注册
            测试步骤：只输入账号，不输入密码，点击登录
        '''
        print ("------只输入手机号测试------")
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)

        login_page = LoginPage.Login(self.driver)
        login_page.input_phone(self.phone_num_right)
        login_page.click_login_button()

        result  =self.driver.find_element_by_class_name('UserErrorTips').text.split()[0]
        print(result)
        except_result = u'请输入密码'
        self.assertEqual(result,except_result,msg="%s等于%s"%(result,except_result))

    def test_Login_03(self):
        u'''UI-03
            前提条件：手机号已经被注册
            测试步骤：输入未注册账号，输入密码，点击登录
        '''
        print ("------输入未注册手机号测试------")
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)

        login_page = LoginPage.Login(self.driver)
        login_page.input_phone(self.phone_num_wrong)
        login_page.input_pwd(self.phone_num_wrong)
        login_page.click_login_button()

        result  =self.driver.find_element_by_class_name('UserErrorTips').text.split()[0]
        print(result)
        except_result = u'你的手机号还没注册啦！'
        self.assertEqual(result,except_result,msg="%s等于%s"%(result,except_result))
    def test_Login_04(self):
        u'''UI-04
            前提条件：手机号已经被注册
            测试步骤：输入正确账号，输入错误密码，点击登录
        '''
        print ("------输入正确手机号，错误密码测试------")
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)

        login_page = LoginPage.Login(self.driver)
        login_page.input_phone(self.phone_num_right)
        login_page.input_pwd(self.phone_num_wrong)
        login_page.click_login_button()

        result  =self.driver.find_element_by_class_name('UserErrorTips').text.split()[0]
        print(result)
        except_result = u'用户名或者密码不正确'
        self.assertEqual(result,except_result,msg="%s等于%s"%(result,except_result))

    def test_Login_05(self):
        u'''UI-05
            前提条件：手机号已经被注册
            测试步骤：输入正确账号，输入正确密码，点击登录
        '''
        print ("------输入正确手机号，错误密码测试------")
        self.driver.get(self.base_url)
        self.driver.implicitly_wait(10)

        login_page = LoginPage.Login(self.driver)
        login_page.input_phone(self.phone_num_right)
        login_page.input_pwd(self.phone_num_right)
        login_page.click_login_button()
        time.sleep(5)
        result = self.driver.current_url
        print(result)
        except_result = "https://www.kuaikanmanhua.com"
        self.assertEqual(result,except_result,msg="%s等于%s"%(result,except_result))

    def tearDown(self):
        self.driver.close()
if __name__ == '__main__':
    unittest.main()
