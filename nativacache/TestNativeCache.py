import unittest

from nativacache.NativeCache import NativeCache


class MyTestCase(unittest.TestCase):

    def test_put(self):
        nd = NativeCache(17)
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

    def test_put_2(self):
        nd = NativeCache(17)
        nd.put('0', '0')
        self.assertEqual(nd.__str__(), '14,0,0|')

        nd.put('1', '1')
        self.assertEqual(nd.__str__(), '14,0,0|15,1,1|')

        nd.put('2', '2')
        self.assertEqual(nd.__str__(), '14,0,0|15,1,1|16,2,2|')

        nd.put('3', '3')
        self.assertEqual(nd.__str__(), '0,3,3|14,0,0|15,1,1|16,2,2|')

        nd.put('4', '4')
        self.assertEqual(nd.__str__(), '0,3,3|1,4,4|14,0,0|15,1,1|16,2,2|')

        nd.put('5', '5')
        self.assertEqual(nd.__str__(), '0,3,3|1,4,4|2,5,5|14,0,0|15,1,1|16,2,2|')

        nd.put('5', '5')
        self.assertEqual(nd.__str__(), '0,3,3|1,4,4|2,5,5|14,0,0|15,1,1|16,2,2|')
        self.assertEqual(nd.hits[2], 0)
        self.assertEqual(nd.get('5'), '5')
        self.assertEqual(nd.hits[2], 1)

        i = 6
        while i <= 9:
            nd.put(i.__str__(), i.__str__())
            i += 1
        self.assertEqual(nd.__str__(), '0,3,3|1,4,4|2,5,5|3,6,6|4,7,7|5,8,8|6,9,9|14,0,0|15,1,1|16,2,2|')

        letters = ('A', 'B', 'C', 'D', 'E', 'F', 'G')
        for letter in letters:
            nd.put(letter, letter)
        self.assertEqual(nd.__str__(), '0,3,3|1,4,4|2,5,5|3,6,6|4,7,7|5,8,8|6,9,9|7,A,A|8,B,B|9,C,C|10,D,D|11,E,E|12,F,F|13,G,G|14,0,0|15,1,1|16,2,2|')

        i = 0
        letters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', '0', '1', '2', '3', '4', '6', '7', '8', '9')
        while i < 10:
            for let in letters:
                nd.get(let)
            i += 1

        self.assertEqual(nd.hits[2], 1)
        nd.put('Z', 'Z')
        self.assertEqual(nd.__str__(), '0,3,3|1,4,4|2,Z,Z|3,6,6|4,7,7|5,8,8|6,9,9|7,A,A|8,B,B|9,C,C|10,D,D|11,E,E|12,F,F|13,G,G|14,0,0|15,1,1|16,2,2|')

    def test_get(self):
        nd = NativeCache(17)
        nd.put('3', 'Hello')
        self.assertEqual(nd.get('3'), 'Hello')
        self.assertEqual(nd.get('4'), None)

if __name__ == '__main__':
    unittest.main()
