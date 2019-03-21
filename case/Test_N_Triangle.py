# -*- coding:utf-8 -*-


import unittest
import sys
sys.path.append(r'/Users/chenhang/Desktop/pythonFile/python/untitled/practice/pyhton-unittest-jenkins/model')
from inputs import Triangle_output



class Test_N_Triangle(unittest.TestCase):
    def setUp(self):
        """调用测试数据提供测试"""
        pass



    def test_N_Triangle(self):
        self.assertEqual(Triangle_output('2', '1', '1'), "非三角形")
        self.assertEqual(Triangle_output('9', '2.3', '1.2'), "非三角形")

