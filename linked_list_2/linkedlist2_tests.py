import unittest
from linkedlist2 import LinkedList2
from linkedlist2 import Node


class MyTestCase(unittest.TestCase):

    def test_find(self):
        ll = LinkedList2()
        self.assertEqual(ll.find(5), None)

        ll = LinkedList2().fill(1, 2, 3)
        self.assertEqual(ll.find(5), None)

        node1 = Node(1)
        node2 = Node(1)
        node3 = Node(1)
        ll = LinkedList2()
        ll.add_in_tail(node1)
        ll.add_in_tail(node2)
        ll.add_in_tail(node3)
        self.assertEqual(ll.find(1), node1)

    def test_find_all(self):
        ll = LinkedList2()
        self.assertEqual(ll.find_all(5), [])

        node1 = Node(1)
        node2 = Node(1)
        node3 = Node(1)
        ll = LinkedList2()
        ll.add_in_tail(node1)
        ll.add_in_tail(node2)
        ll.add_in_tail(node3)
        self.assertEqual(ll.find_all(1), [node1, node2, node3])

    def test_delete_one(self):
        ll = LinkedList2()
        ll.delete(0)
        self.assertEqual(ll, LinkedList2())

        ll = LinkedList2().fill(1, 1, 1)
        ll.delete(1)
        self.assertEqual(ll, LinkedList2().fill(1, 1))

        ll = LinkedList2().fill(1, 2, 3)
        ll.delete(3)
        self.assertEqual(ll, LinkedList2().fill(1, 2))
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.tail.value, 2)

    def test_delete_all(self):
        ll = LinkedList2()
        ll.delete(0, True)
        self.assertEqual(ll, LinkedList2())

        ll = LinkedList2().fill(1, 1, 1)
        ll.delete(1, True)
        self.assertEqual(ll, LinkedList2())

        ll = LinkedList2().fill(1, 1, 1, 2, 3)
        ll.delete(1, True)
        self.assertEqual(ll, LinkedList2().fill(2, 3))
        self.assertEqual(ll.head.value, 2)
        self.assertEqual(ll.tail.value, 3)

        ll = LinkedList2().fill(1, 1, 1, 2, 3, 1, 1)
        ll.delete(1, True)
        self.assertEqual(ll, LinkedList2().fill(2, 3))
        self.assertEqual(ll.head.value, 2)
        self.assertEqual(ll.tail.value, 3)

        ll = LinkedList2().fill(2, 3, 1, 1)
        ll.delete(1, True)
        self.assertEqual(ll, LinkedList2().fill(2, 3))
        self.assertEqual(ll.head.value, 2)
        self.assertEqual(ll.tail.value, 3)

    def test_insert(self):
        ll = LinkedList2()
        ll.insert(None, Node(0))
        self.assertEqual(ll, LinkedList2().fill(0))
        self.assertEqual(ll.head.value, 0)
        self.assertEqual(ll.tail.value, 0)

        ll = LinkedList2()
        node1 = Node(1)
        node2 = Node(2)
        ll.add_in_tail(node1)
        ll.insert(node1, node2)
        self.assertEqual(ll, LinkedList2().fill(1, 2))
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.tail.value, 2)

        ll = LinkedList2()
        node1 = Node(1)
        node2 = Node(2)
        ll.add_in_tail(node1)
        ll.insert(None, node2)
        self.assertEqual(ll, LinkedList2().fill(1, 2))
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.tail.value, 2)

        ll = LinkedList2()
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        ll.add_in_tail(node1)
        ll.add_in_tail(node3)
        ll.insert(node1, node2)
        self.assertEqual(ll, LinkedList2().fill(1, 2, 3))
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.tail.value, 3)

    def test_add_in_head(self):
        ll = LinkedList2()
        ll.add_in_head(Node(0))
        self.assertEqual(ll, LinkedList2().fill(0))
        self.assertEqual(ll.head.value, 0)
        self.assertEqual(ll.tail.value, 0)

        ll = LinkedList2()
        node1 = Node(1)
        node2 = Node(2)
        ll.add_in_tail(node2)
        ll.add_in_head(node1)
        self.assertEqual(ll, LinkedList2().fill(1, 2))
        self.assertEqual(ll.head.value, 1)
        self.assertEqual(ll.tail.value, 2)



if __name__ == '__main__':
    unittest.main()
