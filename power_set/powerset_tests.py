import time
import unittest

from power_set.PowerSet import PowerSet


class MyTestCase(unittest.TestCase):

    def test_put(self):
        set1 = PowerSet()
        set1.put(1)
        self.assertEqual(set1.__str__(), '1,')

        set1.put(2)
        self.assertEqual(set1.__str__(), '1,2,')

        set1.put(1)
        self.assertEqual(set1.__str__(), '1,2,')

    def test_remove(self):
        set1 = PowerSet()
        set1.put(1)
        set1.put(2)
        set1.put(3)
        self.assertEqual(set1.__str__(), '1,2,3,')

        result = set1.remove(1)
        self.assertEqual(set1.__str__(), '2,3,')
        self.assertEqual(result, True)

        result = set1.remove(10)
        self.assertEqual(set1.__str__(), '2,3,')
        self.assertEqual(result, False)

    def test_interseption(self):
        set1 = PowerSet()
        set2 = PowerSet()

        i = 0
        while i < 20_000:
            set1.put(i)
            i += 1

        i = 19_998
        while i < 39_000:
            set2.put(i)
            i += 1

        start_time = time.time()
        intersection = set1.intersection(set2)
        dt = time.time() - start_time
        print("--- %s seconds ---" % dt)
        self.assertLess(dt, 2)
        self.assertEqual(intersection.__str__(), '19998,19999,')

        set3 = PowerSet()
        set3.put(100_000)
        intersection = set1.intersection(set3)
        self.assertEqual(intersection.__str__(), '')

    def test_interseption_2(self):
        set1 = PowerSet()
        set2 = PowerSet()

        set1.put(20_000)
        set1.put(2)
        set2.put(20_000)

        intersection = set1.intersection(set2)
        self.assertEqual(intersection.__str__(), '20000,')

    def test_union(self):
        set1 = PowerSet()
        set2 = PowerSet()
        i = 0
        while i < 20_000:
            set1.put(i)
            i += 1

        i = 19_998
        while i < 39_000:
            set2.put(i)
            i += 1

        start_time = time.time()
        result_set = set1.union(set2)
        dt = time.time() - start_time
        print("--- %s seconds ---" % dt)
        self.assertLess(dt, 2)
        test_set = PowerSet()
        i = 0
        while i < 39_000:
            test_set.put(i)
            i += 1
        self.assertEqual(result_set.__str__(), test_set.__str__())

        set3 = PowerSet()
        result_set = set1.union(set3)
        self.assertEqual(result_set.__str__(), set1.__str__())

    def test_difference(self):
        set1 = PowerSet()
        set2 = PowerSet()
        i = 0
        while i < 20_001:
            set1.put(i)
            i += 1

        i = 0
        while i < 20_000:
            set2.put(i)
            i += 1

        start_time = time.time()
        result_set = set1.difference(set2)
        dt = time.time() - start_time
        print("--- %s seconds ---" % dt)
        self.assertLess(dt, 2)
        self.assertEqual(result_set.__str__(), '20000,')

        set3 = PowerSet()
        i = 0
        while i < 20_001:
            set3.put(i)
            i += 1
        result_set = set1.difference(set3)
        self.assertEqual(result_set.__str__(), '')

    def test_is_subset(self):
        set1 = PowerSet()
        set2 = PowerSet()
        i = 0
        while i < 20_000:
            set1.put(i)
            i += 1

        i = 0
        while i < 10_00:
            set2.put(i)
            i += 1

        start_time = time.time()
        result = set1.issubset(set2)
        dt = time.time() - start_time
        print("--- %s seconds ---" % dt)
        self.assertLess(dt, 2)
        self.assertEqual(result, True)

        set3 = PowerSet()
        i = 0
        while i < 40_000:
            set3.put(i)
            i += 1
        result = set1.issubset(set3)
        self.assertEqual(result, False)

        set4 = PowerSet()
        i = 10_000
        while i < 30_000:
            set4.put(i)
            i += 1
        result = set1.issubset(set4)
        self.assertEqual(result, False)




if __name__ == '__main__':
    unittest.main()
