from linkedlist import LinkedList
from linkedlist import Node

ll = LinkedList().fill_from_array([1, 1, 1, 1, 2, 3, 4, 1, 1, 1])
ll.delete(1, True)
print(ll)