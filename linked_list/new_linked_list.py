from linkedlist import LinkedList
from linkedlist import Node


def create_linkedlist_from_sum(linkedlist1, linkedlist2):
    if linkedlist1.len() == linkedlist2.len():
        new_linkedlist = LinkedList()
        node1 = linkedlist1.head
        node2 = linkedlist2.head
        while node1 is not None:
            new_linkedlist.add_in_tail(Node(node1.value + node2.value))
            node1 = node1.next
            node2 = node2.next
        return new_linkedlist

