# import unittest
# #
# #
# # class TestStringMethods(unittest.TestCase):
# #
# #     def test_upper(self):
# #         self.assertEqual('foo'.upper(), 'FOO')
# #
# #     def test_isupper(self):
# #         """
# #         test methond isupper
# #         :return:
# #         """
# #         self.assertTrue('FOO'.isupper())
# #         self.assertFalse('Foo'.isupper())
# #
# #     def test_split(self):
# #         s = 'hello world'
# #         self.assertEqual(s.split(), ['hello', 'world'])
# #         # check that s.split fails when the separator is not a string
# #         with self.assertRaises(TypeError):
# #             s.split(2)
# #
# #
# # if __name__ == '__main__':
# #     unittest.main(verbosity=2)

# import os
#
#
# p = os.fspath(os.path.abspath(__file__))
# print(p)
# print(os.path.abspath('.'))

import unittest


class Test(unittest.TestCase):

    def setUp(self):
        print('run case')

    def tearDown(self):
        print('case end')

    def test_test(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
