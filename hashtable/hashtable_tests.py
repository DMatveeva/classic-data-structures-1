import unittest
from Hashtable import HashTable


class MyTestCase(unittest.TestCase):

    def test_hash_fun(self):
        ht = HashTable(17, 3)
        string = 'hello'
        self.assertEqual(ht.hash_fun(string), 5)

        string2 = 'oellh'
        self.assertEqual(ht.hash_fun(string2), 5)

    def test_seek_slot(self):
        ht = HashTable(17, 3)

        string = 'hello'
        self.assertEqual(ht.seek_slot(string), 5)

        string = 'oellh'
        self.assertEqual(ht.seek_slot(string), 5)

    def test_put(self):
        ht = HashTable(17, 3)

        string = 'hello'
        self.assertEqual(ht.put(string), 5)

        string = 'oellh'
        self.assertEqual(ht.put(string), 8)

        self.assertEqual(ht.put(''), 0)
        self.assertEqual(ht.put(None), None)
        self.assertEqual(ht.put(1), None)
        self.assertEqual(ht.put('2'), 16)
        self.assertEqual(ht.put('C'), 2)



    def test_find(self):
        ht = HashTable(17, 3)

        string = 'hello'
        ht.put(string)
        self.assertEqual(ht.find(string), 5)

        string = 'oellh'
        ht.put(string)
        self.assertEqual(ht.find(string), 8)

        string = 'oelhl'
        ht.put(string)
        self.assertEqual(ht.find(string), 11)

        string = 'loelh'
        ht.put(string)
        self.assertEqual(ht.find(string), 14)

        string = 'leolh'
        ht.put(string)
        self.assertEqual(ht.find(string), 0)

        string = 'elolh'
        ht.put(string)
        self.assertEqual(ht.find(string), 3)

        string = 'elohl'
        ht.put(string)
        self.assertEqual(ht.find(string), 6)

        string = 'eohll'
        ht.put(string)
        self.assertEqual(ht.find(string), 9)

        string = 'lhoel'
        ht.put(string)
        self.assertEqual(ht.find(string), 12)

        string = 'lheol'
        ht.put(string)
        self.assertEqual(ht.find(string), 15)

        string = 'hleol'
        ht.put(string)
        self.assertEqual(ht.find(string), 1)

        string = 'hlelo'
        ht.put(string)
        self.assertEqual(ht.find(string), 4)

        string = 'ehllo'
        ht.put(string)
        self.assertEqual(ht.find(string), 7)

        string = 'eholl'
        ht.put(string)
        self.assertEqual(ht.find(string), 10)

        string = 'holle'
        ht.put(string)
        self.assertEqual(ht.find(string), 13)

        string = 'eollh'
        ht.put(string)
        self.assertEqual(ht.find(string), 16)

        string = 'ellho'
        ht.put(string)
        self.assertEqual(ht.find(string), 2)

        string = 'lleho'
        ht.put(string)
        self.assertEqual(ht.find(string), None)

if __name__ == '__main__':
    unittest.main()
