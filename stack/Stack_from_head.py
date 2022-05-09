from linked_list.linkedlist import LinkedList, Node


class StackFromHead:
    def __init__(self):
        self.stack = LinkedList()

    def size(self):
        return self.stack.len()

    def pop(self):
        if self.size() == 0:
            return None
        else:
            element = self.stack.head.value
            self.stack.head = self.stack.head.next
            return element

    def push(self, value):
        self.stack.insert(None, Node(value))

    def peek(self):
        if self.size() == 0:
            return None
        else:
            return self.stack.head.value

    def __str__(self):
        return self.stack.__str__()
