import unittest

from native_dictionary.NativeDictionary import NativeDictionary


class MyTestCase(unittest.TestCase):

    def test_put(self):

        nd = NativeDictionary(17)
        nd.put('3', 'Hi')
        self.assertEqual(nd.__str__(), '0,3,Hi|')

        nd.put('3', 'Hello')
        self.assertEqual(nd.__str__(), '0,3,Hello|')

        nd.put('5', 'Darya')
        self.assertEqual(nd.__str__(), '0,3,Hello|2,5,Darya|')

        nd.put('2', 'Coffee')
        self.assertEqual(nd.__str__(), '0,3,Hello|2,5,Darya|16,2,Coffee|')

        nd.put('D', 'Doll')
        self.assertEqual(nd.__str__(), '0,3,Hello|1,D,Doll|2,5,Darya|16,2,Coffee|')

    def test_is_key(self):
        nd = NativeDictionary(17)
        nd.put('3', 'Hi')
        self.assertEqual(nd.is_key('3'), True)
        self.assertEqual(nd.is_key('4'), False)

    def test_get(self):
        nd = NativeDictionary(17)
        nd.put('3', 'Hello')
        self.assertEqual(nd.get('3'), 'Hello')
        self.assertEqual(nd.get('4'), None)

if __name__ == '__main__':
    unittest.main()
