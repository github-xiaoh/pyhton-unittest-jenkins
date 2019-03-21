# -*- coding:utf-8 -*-

from case import Test_Triangle,Test_E_Triangle,Test_I_Triangle,Test_N_Triangle,Test_Error_data,Test_R_Triangle,Test_I_R_Triangle
import unittest



def suite():

    suite = unittest.TestSuite()

    # 将测试用例加入到测试容器（套件）中

    suite.addTest(unittest.makeSuite(Test_Triangle.Test_Triangle))
    suite.addTest(unittest.makeSuite(Test_E_Triangle.Test_E_Triangle))
    suite.addTest(unittest.makeSuite(Test_I_Triangle.Test_I_Triangle))
    suite.addTest(unittest.makeSuite(Test_N_Triangle.Test_N_Triangle))
    suite.addTest(unittest.makeSuite(Test_Error_data.Test_Error_data))
    suite.addTest(unittest.makeSuite(Test_R_Triangle.Test_R_Triangle))
    suite.addTest(unittest.makeSuite(Test_I_R_Triangle.Test_I_R_Triangle))

    # 执行测试套件
    # runner = unittest.TextTestRunner()
    # runner.run(suite)
    return suite

