import unittest

from stack.Stack_from_head import StackFromHead


class MyTestCase(unittest.TestCase):
    def test_size(self):
        stack = StackFromHead()
        self.assertEqual(stack.size(), 0)

        stack.push(0)
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.size(), 3)

    def test_push(self):
        stack = StackFromHead()
        stack.push(0)
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.__str__(), '2, 1, 0, ')

    def test_pop(self):
        stack = StackFromHead()
        el = stack.pop()
        self.assertEqual(el, None)
        self.assertEqual(stack.__str__(), '')

        stack.push(0)
        el2 = stack.pop()
        self.assertEqual(el2, 0)
        self.assertEqual(stack.__str__(), '')

        stack.push(0)
        stack.push(1)
        stack.push(2)
        stack.push(3)
        el2 = stack.pop()
        self.assertEqual(el2, 3)
        self.assertEqual(stack.__str__(), '2, 1, 0, ')

    def test_peek(self):
        stack = StackFromHead()
        el = stack.peek()
        self.assertEqual(el, None)
        self.assertEqual(stack.__str__(), '')

        stack.push(0)
        el = stack.peek()
        self.assertEqual(el, 0)
        self.assertEqual(stack.__str__(), '0, ')


if __name__ == '__main__':
    unittest.main()
