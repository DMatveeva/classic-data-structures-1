import unittest

from deque.Deque import Deque
from is_palindrome import is_palindrome


class MyTestCase(unittest.TestCase):

    def test_addFront(self):
        deque = Deque()
        deque.addFront(0)
        self.assertEqual(deque.__str__(), '0,')

        deque.addFront(1)
        deque.addFront(2)
        self.assertEqual(deque.__str__(), '2,1,0,')

    def test_addTail(self):
        deque = Deque()
        deque.addFront(0)
        deque.addFront(1)
        deque.addFront(2)
        deque.addTail(3)
        deque.addTail(4)
        self.assertEqual(deque.__str__(), '2,1,0,3,4,')

    def test_removeFront(self):
        deque = Deque()
        el = deque.removeFront()
        self.assertEqual(el, None)
        self.assertEqual(deque.__str__(), '')

        deque.addFront(0)
        deque.addFront(1)
        deque.addFront(2)
        el = deque.removeFront()
        self.assertEqual(el, 2)
        self.assertEqual(deque.__str__(), '1,0,')

    def test_removeTail(self):
        deque = Deque()
        el = deque.removeFront()
        self.assertEqual(el, None)
        self.assertEqual(deque.__str__(), '')

        deque.addFront(0)
        deque.addFront(1)
        deque.addFront(2)
        el = deque.removeTail()
        self.assertEqual(el, 0)
        self.assertEqual(deque.__str__(), '2,1,')

    def test_is_palindrome(self):
        string = 'Poor Dan is in a droop'
        self.assertEqual(is_palindrome(string), True)

        string = 'Alice'
        self.assertEqual(is_palindrome(string), False)

        string = ''
        self.assertEqual(is_palindrome(string), False)

        string = None
        self.assertEqual(is_palindrome(string), False)

        string = 'Sit on a potato pan, Otis.'
        self.assertEqual(is_palindrome(string), True)








if __name__ == '__main__':
    unittest.main()
