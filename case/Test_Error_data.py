# -*- coding:utf-8 -*-


import unittest
import sys
sys.path.append(r'/Users/chenhang/Desktop/pythonFile/python/untitled/practice/pyhton-unittest-jenkins/model')
from inputs import Triangle_output



class Test_Error_data(unittest.TestCase):
    def setUp(self):
        """调用测试数据提供测试"""
        pass


    def test_Error_data(self):
        self.assertEqual(Triangle_output('w', '1', '1'), "输入值错误")
        self.assertEqual(Triangle_output('1', '时代光华', '1'), "输入值错误")
        self.assertEqual(Triangle_output('w', '1', '￥%……&ddw12'), "输入值错误")