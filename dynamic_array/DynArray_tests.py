import unittest
from DynArray import DynArray


class MyTestCase(unittest.TestCase):
    def test_insert(self):
        da = DynArray()
        da.append(0)
        da.append(1)
        da.append(2)
        da.append(3)
        da.append(4)
        da.append(5)
        da.insert(3, 30)
        self.assertEqual(da, DynArray().fill(0, 1, 2, 30, 3, 4, 5))
        self.assertEqual(da.capacity, 16)
        self.assertEqual(da.count, 7)

        da = DynArray()
        da.fill(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
        da.insert(14, 140)
        self.assertEqual(da, DynArray().fill(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 140, 14, 15))
        self.assertEqual(da.capacity, 32)
        self.assertEqual(da.count, 17)

        da = DynArray()
        da.fill(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
        with self.assertRaises(IndexError) as context:
            da.insert(18, 140)

if __name__ == '__main__':
    unittest.main()
