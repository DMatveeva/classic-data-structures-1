import unittest
from OrderedList import OrderedList
from OrderedList import OrderedStringList


class MyTestCase(unittest.TestCase):

    def test_add_asc(self):
        ol = OrderedList(True)
        ol.add(0)
        self.assertEqual(ol.__str__(), '0,')
        ol.add(5)
        self.assertEqual(ol.__str__(), '0,5,')
        ol.add(2)
        self.assertEqual(ol.__str__(), '0,2,5,')
        ol.add(7)
        self.assertEqual(ol.__str__(), '0,2,5,7,')
        ol.add(-1)
        self.assertEqual(ol.__str__(), '-1,0,2,5,7,')
        ol.add(7)
        self.assertEqual(ol.__str__(), '-1,0,2,5,7,7,')

    def test_add_desc(self):
        ol = OrderedList(False)
        ol.add(0)
        self.assertEqual(ol.__str__(), '0,')
        ol.add(5)
        self.assertEqual(ol.__str__(), '5,0,')
        ol.add(2)
        self.assertEqual(ol.__str__(), '5,2,0,')
        ol.add(7)
        self.assertEqual(ol.__str__(), '7,5,2,0,')
        ol.add(-1)
        self.assertEqual(ol.__str__(), '7,5,2,0,-1,')
        ol.add(7)
        self.assertEqual(ol.__str__(), '7,7,5,2,0,-1,')
        ol.add(-1)
        self.assertEqual(ol.__str__(), '7,7,5,2,0,-1,-1,')

    def test_len(self):
        ol = OrderedList(True)
        self.assertEqual(ol.len(), 0)
        ol.add(0)
        ol.add(5)
        self.assertEqual(ol.len(), 2)

    def test_delete_asc(self):
        ol = OrderedList(True)
        ol.add(0)
        ol.add(5)
        ol.add(2)
        ol.add(7)
        ol.add(-1)
        ol.delete(-1)
        self.assertEqual(ol.__str__(), '0,2,5,7,')
        ol.delete(7)
        self.assertEqual(ol.__str__(), '0,2,5,')
        ol.delete(8)
        ol.delete(2)
        self.assertEqual(ol.__str__(), '0,5,')
        ol.delete(10)
        self.assertEqual(ol.__str__(), '0,5,')

    def test_delete_desc(self):
        ol = OrderedList(False)
        ol.add(0)
        ol.add(5)
        ol.add(2)
        ol.add(7)
        ol.add(-1)
        self.assertEqual(ol.__str__(), '7,5,2,0,-1,')
        ol.delete(-1)
        self.assertEqual(ol.__str__(), '7,5,2,0,')
        ol.delete(7)
        self.assertEqual(ol.__str__(), '5,2,0,')
        ol.delete(8)
        ol.delete(2)
        self.assertEqual(ol.__str__(), '5,0,')
        ol.delete(10)
        self.assertEqual(ol.__str__(), '5,0,')

        ol.clean(True)
        ol.add(1)
        ol.delete(1)
        self.assertEqual(ol.__str__(), '')

    def test_find(self):
        ol = OrderedList(False)
        ol.add(0)
        ol.add(5)
        ol.add(2)
        ol.add(7)
        ol.add(-1)
        el = ol.find(0).value
        self.assertEqual(el, 0)
        el = ol.find(10)
        self.assertEqual(el, None)





if __name__ == '__main__':
    unittest.main()
