import unittest

from linked_list.new_linked_list import create_linkedlist_from_sum
from linkedlist import LinkedList
from linkedlist import Node


class MyTestCase(unittest.TestCase):

    def test_equals_empty_ll(self):
        empty_ll_1 = LinkedList()
        empty_ll_2 = LinkedList()
        self.assertEqual(empty_ll_1, empty_ll_2)

    def test_equals_same_ll(self):
        ll_1 = LinkedList().fill_from_array([1, 1, 1, 4, 0])
        ll_2 = LinkedList().fill_from_array([1, 1, 1, 4, 0])
        self.assertEqual(ll_1, ll_2)

    def test_equals_not_same(self):
        ll_1 = LinkedList().fill_from_array([1, 1])
        ll_2 = LinkedList().fill_from_array([1, 1, 1, 4, 0])
        self.assertNotEqual(ll_1, ll_2)

    def test_delete_from_empty_ll(self):
        ll = LinkedList()
        ll.delete(1)
        self.assertEqual(ll, LinkedList())

    def test_delete_none_from_empty_ll(self):
        ll = LinkedList()
        ll.delete(None)
        self.assertEqual(ll, LinkedList())

    def test_delete_present_element_from_single_element_ll(self):
        ll = LinkedList().fill_from_array([1])
        ll.delete(1)
        self.assertEqual(ll, LinkedList())
        self.assertEqual(ll.tail, None)
        self.assertEqual(ll.head, None)

    def test_delete_not_present_element_from_single_element_ll(self):
        ll = LinkedList().fill_from_array([1])
        ll.delete(2)
        self.assertEqual(ll, LinkedList().fill_from_array([1]))
        self.assertEqual(ll.tail.value, 1)
        self.assertEqual(ll.head.value, 1)

    def test_delete_all_from_head(self):
        ll = LinkedList().fill_from_array([1, 2, 1, 1, 2, 3, 4, 1, 1])
        ll.delete(1, True)
        self.assertEqual(ll, LinkedList().fill_from_array([2, 2, 3, 4]))
        self.assertEqual(ll.tail.value, 4)
        self.assertEqual(ll.head.value, 2)

    def test_delete_all(self):
        ll = LinkedList().fill_from_array([1, 1, 1, 1, 1, 1, 1, 1, 1, 2])
        ll.delete(2, True)
        self.assertEqual(ll, LinkedList().fill_from_array([1, 1, 1, 1, 1, 1, 1, 1, 1]))

    def test_delete_1(self):
        ll = LinkedList().fill_from_array([1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1])
        ll.delete(1, True)
        self.assertEqual(ll, LinkedList().fill_from_array([2]))
        self.assertEqual(ll.tail.value, 2)

    def test_delete_2(self):
        ll = LinkedList().fill_from_array([1, 1, 1])
        ll.delete(1, True)
        self.assertEqual(ll, LinkedList().fill_from_array([]))
        self.assertEqual(ll.head, None)
        self.assertEqual(ll.tail, None)

    def test_delete_present_element_from_big_ll(self):
        ll = LinkedList().fill_from_array([k for k in range(1,10000)])
        ll.delete(20)

        array_2 = []
        for k in range(1, 10000):
            if k != 20:
                array_2 += [k]
        ll_2 = LinkedList().fill_from_array(array_2)
        self.assertEqual(ll, ll_2)
        self.assertEqual(ll.head.value, 1)


    def test_find_all_empty_ll(self):
        ll = LinkedList()
        result = ll.find_all(0)
        self.assertEqual(result, [])

    def test_find_all_none_in_empty_ll(self):
        ll = LinkedList().fill_from_array([None])
        result = ll.find_all(None)
        self.assertEqual(result, [ll.head])

    def test_find_all(self):
        ll = LinkedList().fill_from_array([1, 1, 2, 3, 4, 1])
        result = ll.find_all(1)
        ll.delete(2)
        ll.delete(3)
        ll.delete(4)
        list_test = list()
        node = ll.head
        while node is not None:
            list_test.append(node)
            node = node.next
        self.assertEqual(result, list_test)

    def test_find_all_in_big_ll(self):
        array = [1] * 1000
        ll = LinkedList().fill_from_array(array)
        result = ll.find_all(1)
        list_test = list()
        node = ll.head
        while node is not None:
            list_test.append(node)
            node = node.next
        self.assertEqual(result, list_test)

    def test_len(self):
        array = [1] * 1000
        ll = LinkedList().fill_from_array(array)
        self.assertEqual(ll.len(), 1000)

    def test_insert_1(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        ll = LinkedList()
        ll.add_in_tail(node1)
        ll.add_in_tail(node2)
        ll.add_in_tail(node3)
        ll.insert(node3, Node(4))
        self.assertEqual(ll, LinkedList().fill_from_array([1, 2, 3, 4]))

    def test_insert_2(self):
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        ll = LinkedList()
        ll.add_in_tail(node1)
        ll.add_in_tail(node2)
        ll.add_in_tail(node3)
        ll.insert(node2, Node(4))
        self.assertEqual(ll, LinkedList().fill_from_array([1, 2, 4, 3]))

    def test_insert_3(self):
        ll = LinkedList()
        ll.insert(None, Node(4))
        self.assertEqual(ll, LinkedList().fill_from_array([4]))
        self.assertEqual(ll.tail.value, 4)

    def test_sum(self):
        ll1 = LinkedList().fill_from_array([1, 1, 1, 1])
        ll2 = LinkedList().fill_from_array([1, 1, 1, 1])
        new_ll = create_linkedlist_from_sum(ll1, ll2)
        self.assertEqual(new_ll, LinkedList().fill_from_array([2, 2, 2, 2]))

        ll1 = LinkedList()
        ll2 = LinkedList()
        new_ll = create_linkedlist_from_sum(ll1, ll2)
        self.assertEqual(new_ll, LinkedList())




if __name__ == '__main__':
    unittest.main()
