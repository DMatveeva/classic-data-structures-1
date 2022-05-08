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
        da.insert(16, 150)
        self.assertEqual(da.capacity, 32)
        self.assertEqual(da.count, 17)
        self.assertEqual(da, DynArray().fill(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 150))

        da = DynArray()
        da.fill(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
        with self.assertRaises(IndexError) as context:
            da.insert(18, 140)

    def test_delete(self):
        da = DynArray()
        da.append(0)
        da.append(1)
        da.append(2)
        da.append(3)
        da.append(4)
        da.append(5)
        da.delete(3)
        self.assertEqual(da.capacity, 16)
        self.assertEqual(da.count, 5)
        self.assertEqual(da, DynArray().fill(0, 1, 2, 4, 5))

        da = DynArray()
        da.fill(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16)
        da.delete(16)
        self.assertEqual(da.capacity, 32)
        self.assertEqual(da.count, 16)
        array = DynArray().fill(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
        self.assertEqual(da, array)

        da.delete(1)
        self.assertEqual(da.count, 15)
        self.assertEqual(da.capacity, 21)
        array = DynArray().fill(0, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15)
        self.assertEqual(da, array)

        with self.assertRaises(IndexError) as context:
            da.delete(20)


if __name__ == '__main__':
    unittest.main()
