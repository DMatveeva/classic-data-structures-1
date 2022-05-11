import unittest
from queue.Queue import Queue
from queue.rotate_queue import rotate_queue


class MyTestCase(unittest.TestCase):

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue(0)
        self.assertEqual(queue.__str__(), '0,')

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.__str__(), '0,1,2,3,')

    def test_dequeue(self):
        queue = Queue()
        queue.enqueue(0)
        el = queue.dequeue()
        self.assertEqual(el, 0)
        self.assertEqual(queue.__str__(), '')

        el = queue.dequeue()
        self.assertEqual(el, None)
        self.assertEqual(queue.__str__(), '')

        queue.enqueue(0)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        el = queue.dequeue()
        self.assertEqual(el, 0)
        self.assertEqual(queue.__str__(), '1,2,3,')

    def test_rotate_queue(self):
        queue = Queue()
        queue.enqueue(0)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        rotate_queue(queue, 2)
        self.assertEqual(queue.__str__(), '3,4,0,1,2,')

        queue = Queue()
        queue.enqueue(0)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        rotate_queue(queue, 0)
        self.assertEqual(queue.__str__(), '0,1,2,3,4,')








if __name__ == '__main__':
    unittest.main()
