# -*- coding:utf-8 -*-


import unittest
import sys
sys.path.append(r'/Users/chenhang/Desktop/pythonFile/python/untitled/practice/pyhton-unittest-jenkins/model')

from inputs import Triangle_output



class Test_E_Triangle(unittest.TestCase):
    def setUp(self):
        """调用测试数据提供测试"""
        pass

    def test_E_Triangle(self):
        self.assertEqual(Triangle_output('2', '2', '2'), "等边三角形")
        self.assertEqual(Triangle_output('2.3', '2.3', '2.3'), "等边三角形")