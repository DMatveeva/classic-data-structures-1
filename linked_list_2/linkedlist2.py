class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None


class LinkedList2:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
            item.prev = None
            item.next = None
        else:
            self.tail.next = item
            item.prev = self.tail
        self.tail = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        result = []
        node = self.head
        while node is not None:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def delete(self, val, all=False):
        node = self.head
        while node is not None:
            if node.value == val:
                if node.prev is None and node.next is None:
                    self.head = None
                    self.tail = None
                elif node.prev is None:
                    node.next.prev = None
                    self.head = node.next
                elif node.next is None:
                    node.prev.next = None
                    self.tail = node.prev
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                if not all:
                    return
            node = node.next

    def clean(self):
        self.head = None
        self.tail = None

    def len(self):
        length = 0
        node = self.head
        while node is not None:
            length += 1
            node = node.next
        return length

    def insert(self, afterNode, newNode):
        if afterNode is None:
            self.add_in_tail(newNode)
        else:
            node = self.head
            while node is not None:
                if node == afterNode:
                    if afterNode is self.tail:
                        self.add_in_tail(newNode)
                    else:
                        afterNode.next.prev = newNode
                        newNode.next = afterNode.next
                        newNode.prev = afterNode
                        afterNode.next = newNode
                node = node.next

    def add_in_head(self, newNode):
        if self.head is None:
            newNode.next = None
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.prev = newNode
        self.head = newNode
        newNode.prev = None

    def fill(self, *values):
        for value in values:
            node = Node(value)
            self.add_in_tail(node)
        return self

    def __eq__(self, other):
        if self.head is None and other.head is None:
            return True
        if self.len() != other.len():
            return False
        else:
            node_from_self = self.head
            node_from_other = other.head
            while node_from_other is not None:
                if node_from_self.value != node_from_other.value:
                    return False
                node_from_other = node_from_other.next
                node_from_self = node_from_self.next
        return True

    def __str__(self):
        node = self.head
        string = ''
        while node is not None:
            string += f'{node.value}, '
            node = node.next
        return string
