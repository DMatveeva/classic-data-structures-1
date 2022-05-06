from linkedlist2 import LinkedList2
from linkedlist2 import Node


node1 = Node(1)
node2 = Node(1)
node3 = Node(1)
ll = LinkedList2()
ll.add_in_tail(node1)
ll.add_in_tail(node2)
ll.add_in_tail(node3)
print(ll.head)
print(ll.head.next)
print(ll.tail)
print(ll.find(1))