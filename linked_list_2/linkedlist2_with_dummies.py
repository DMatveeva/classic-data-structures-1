class Node:
    def __init__(self, v):
        self.value = v
        self.prev = None
        self.next = None

    def is_real(self):
        return True


class DummyNode(Node):
    def __init__(self):
        super().__init__("This is error. You shouldn't see this, it's a dummy node.")

    def is_real(self):
        return False


class LinkedList2:
    def __init__(self):
        dummy_head = DummyNode()
        dummy_tail = DummyNode()
        dummy_head.prev = None
        dummy_head.next = dummy_tail
        dummy_tail.prev = dummy_head
        dummy_tail.next = None
        self.head = dummy_head
        self.tail = dummy_tail

    def add_in_tail(self, item):
        self.tail.prev.next = item
        item.prev = self.tail.prev
        item.next = self.tail
        self.tail.prev = item

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val and node.is_real():
                return node
            node = node.next
        return None

    def find_all(self, val):
        result = []
        node = self.head
        while node is not None:
            if node.value == val and node.is_real():
                result.append(node)
            node = node.next
        return result

    def delete(self, val, all=False):
        node = self.head
        while node is not None:
            if node.value == val and node.is_real():
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
        if afterNode is None and self.head is None:
            self.add_in_head(newNode)
        elif afterNode is None and self.head is not None:
            self.add_in_tail(newNode)
        node = self.head
        while node is not self.tail:
            if node == afterNode and node.is_real():
                afterNode.next.prev = newNode
                newNode.next = afterNode.next
                newNode.prev = afterNode
                afterNode.next = newNode
            node = node.next

    def add_in_head(self, newNode):
        self.head.next.prev = newNode
        newNode.next = self.head.next
        newNode.prev = self.head
        self.head.next = newNode

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
