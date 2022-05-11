import unittest
from queue.queue_with_stacks import QueueWithStacks


class MyTestCase(unittest.TestCase):

    def test_enqueue(self):
        queue = QueueWithStacks()
        queue.enqueue(0)
        self.assertEqual(queue.__str__(), 'enqueue: 0,   dequeue: ')

        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.__str__(), 'enqueue: 0,1,2,3,   dequeue: ')

    def test_dequeue(self):
        queue = QueueWithStacks()
        queue.enqueue(0)
        el = queue.dequeue()
        self.assertEqual(el, 0)
        self.assertEqual(queue.__str__(), 'enqueue:    dequeue: ')

        el = queue.dequeue()
        self.assertEqual(el, None)
        self.assertEqual(queue.__str__(), 'enqueue:    dequeue: ')

        queue.enqueue(0)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        el = queue.dequeue()
        self.assertEqual(el, 0)
        self.assertEqual(queue.__str__(), 'enqueue:    dequeue: 3,2,1,')

    def test_size(self):
        queue = QueueWithStacks()
        self.assertEqual(queue.size(), 0)

        queue.enqueue(0)
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.size(), 4)

        queue.dequeue()
        self.assertEqual(queue.size(), 3)









if __name__ == '__main__':
    unittest.main()
