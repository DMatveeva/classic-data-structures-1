import unittest

from deque.Deque import Deque


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




if __name__ == '__main__':
    unittest.main()
