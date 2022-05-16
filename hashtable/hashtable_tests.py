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







if __name__ == '__main__':
    unittest.main()
