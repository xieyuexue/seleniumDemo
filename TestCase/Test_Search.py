# -*- coding: utf-8 -*-
__author__ = 'xieyuexue'
import unittest
from PO import SearchPage
from selenium import webdriver
from Public import Common

class Search(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.base_url = Common.base_url()
        self.keyWord = u'鬼灭之刃'

    def test_Search(self):
        u'''测试搜索框功能'''
        self.driver.get(self.base_url)
        # DashPage.search(self.keyWord)
        dash_page = SearchPage.Dash(self.driver)
        dash_page.input_recipe(self.keyWord)
        print (u'搜索关键字:' + self.keyWord)
        dash_page.click_search_box()

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
