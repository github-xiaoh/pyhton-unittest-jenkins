# -*- coding:utf-8 -*-


import unittest
import sys
sys.path.append(r'/Users/chenhang/Desktop/pythonFile/python/untitled/practice/pyhton-unittest-jenkins/model')
from inputs import Triangle_output



class Test_Triangle(unittest.TestCase):
    def setUp(self):
        """调用测试数据提供测试"""
        pass

    def test_Triangle(self):
        self.assertEqual(Triangle_output('5','3.2','4'),"普通三角形")
        self.assertEqual(Triangle_output('5', '3.7', '3'),"普通三角形")





