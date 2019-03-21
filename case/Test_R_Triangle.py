# -*- coding:utf-8 -*-


import unittest
import sys
sys.path.append(r'/Users/chenhang/Desktop/pythonFile/python/untitled/practice/pyhton-unittest-jenkins/model')
from inputs import Triangle_output
import math



class Test_R_Triangle(unittest.TestCase):
    def setUp(self):
        """调用测试数据提供测试"""
        pass



    def test_R_Triangle(self):
        self.assertEqual(Triangle_output('3', '4', '5'), "直角三角形")
        self.assertEqual(Triangle_output('6', '8', '10'), "直角三角形")