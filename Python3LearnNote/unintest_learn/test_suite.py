#  -*- coding: utf-8 -*-

from Python3LearnNote.unintest_learn.test_mathfunc import *
from Python3LearnNote.unintest_learn.test import *
import unittest
from HTMLTestRunner import HTMLTestRunner


# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#
#     # case name
#     # tests = [TestMathFunc("test_add"), TestMathFunc("test_minus"), TestMathFunc("test_divide")]
#     # suite.addTests(tests)
#
#     # 使用addTests + TestLoader传入模块
#     # suite.addTests(unittest.TestLoader().loadTestsFromName('test_mathfunc')) # 传入单个模块
#
#     suite.addTests(unittest.TestLoader().loadTestsFromNames(['test_mathfunc', 'test'])) # 添加多个模块（文件）
#     # runner = unittest.TextTestRunner(verbosity=2)
#     # runner.run(suite)
#
#     # 将结果输入到文件,报告在同目录下
#     # with open('report.txt', 'a') as f:
#     #     runner = unittest.TextTestRunner(stream=f, verbosity=2)
#     #     runner.run(suite)
#
#     # 使用html文件的报告
#
#     with open('HtmlReport.html', 'w') as f:
#         runner = HTMLTestRunner(stream=f,
#                                 title='test report ',
#                                 description='generated by htmltestrunner',
#                                 verbosity=2
#                                 )
#         runner.run(suite)

# -----------------------------------------------

# if __name__ == '__main__':
#     suite = unittest.TestSuite()
#     suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestMathFunc))
#
#     with open('HTMLReport.html', 'wb') as f:
#         runner = HTMLTestRunner(stream=f,
#                                 title='MathFunc Test Report',
#                                 description='generated by HTMLTestRunner.',
#                                 verbosity=2
#                                 )
#         runner.run(suite)
#
#
# # html输出报告的教程： https://www.jianshu.com/p/6b355b4a87c5

# -----------------------------------------------
