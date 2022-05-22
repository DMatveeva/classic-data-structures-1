import unittest

from bloomfilter.BloomFilter import BloomFilter


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    test1 = '0123456789'
    test2 = '1234567890'
    test3 = '2345678901'
    test4 = '3456789012'
    test5 = '4567890123'
    test6 = '5678901234'
    test7 = '6789012345'
    test8 = '7890123456'
    test9 = '8901234567'
    test10 = '9012345678'

    def test_add(self):
        b_filter = BloomFilter(32)
        b_filter.add(self.test1)
        self.assertEqual(b_filter.is_value(self.test1), True)

        b_filter.add(self.test2)
        self.assertEqual(b_filter.is_value(self.test2), True)

        b_filter.add(self.test3)
        self.assertEqual(b_filter.is_value(self.test3), True)

        b_filter.add(self.test4)
        self.assertEqual(b_filter.is_value(self.test4), True)

        b_filter.add(self.test5)
        self.assertEqual(b_filter.is_value(self.test5), True)

        b_filter.add(self.test6)
        self.assertEqual(b_filter.is_value(self.test6), True)

        b_filter.add(self.test7)
        self.assertEqual(b_filter.is_value(self.test7), True)

        b_filter.add(self.test8)
        self.assertEqual(b_filter.is_value(self.test8), True)

        b_filter.add(self.test9)
        self.assertEqual(b_filter.is_value(self.test9), True)

        b_filter.add(self.test10)
        self.assertEqual(b_filter.is_value(self.test10), True)

        self.assertEqual(b_filter.is_value('hello my friend'), False)




if __name__ == '__main__':
    unittest.main()
