class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

    def is_real(self):
        return True


class DummyNode(Node):
    def is_real(self):
        return False


class LinkedList2:
    def __init__(self):
        dummy_head = DummyNode(None)
        dummy_tail = DummyNode(None)
        dummy_head.prev = None
        dummy_head.next = dummy_tail
        dummy_tail.prev = dummy_head
        dummy_tail.next = None
        self.head = dummy_head
        self.tail = dummy_tail

    def add_in_tail(self, item):
        self.insert(self.tail.prev, item)

    def find(self, val):
        node = self.head.next
        while node is not self.tail:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        result = []
        node = self.head.next
        while node is not self.tail:
            if node.value == val:
                result.append(node)
            node = node.next
        return result

    def delete(self, val, all=False):
        node = self.head.next
        while node is not self.tail:
            if node.value == val:
                node.prev.next = node.next
                node.next.prev = node.prev
                if not all:
                    return
            node = node.next

    def clean(self):
        self.head.next = None
        self.tail.prev = None

    def len(self):
        length = 0
        node = self.head.next
        while node is not self.tail:
            length += 1
            node = node.next
        return length

    def insert(self, afterNode, newNode):
        if afterNode is None:
            afterNode = self.head
        node = self.head
        while node is not self.tail:
            if node == afterNode:
                afterNode.next.prev = newNode
                newNode.next = afterNode.next
                newNode.prev = afterNode
                afterNode.next = newNode
            node = node.next

    def add_in_head(self, newNode):
        self.insert(None, newNode)


