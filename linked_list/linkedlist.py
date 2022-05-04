class Node:

    def __init__(self, v):
        self.value = v
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None

    def add_in_tail(self, item):
        if self.head is None:
            self.head = item
        else:
            self.tail.next = item
        self.tail = item

    def print_all_nodes(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

    def find(self, val):
        node = self.head
        while node is not None:
            if node.value == val:
                return node
            node = node.next
        return None

    def find_all(self, val):
        found_elements = list()
        node = self.head
        while node is not None:
            if node.value == val:
                found_elements.append(node)
            node = node.next
        return found_elements

    def update_tail(self):
        tail = self.head
        while tail is not None:
            if tail.next is None:
                self.tail = tail
            tail = tail.next

    def delete(self, val, all=False):
        # empty ll
        if self.head is None:
            return

        head = self.head
        while head is not None and head.value == val:
            self.head = self.head.next
            if not all:
                return
            head = head.next

        node = self.head
        while node is not None and node.next is not None:
            node_before_duplicates = node
            while node_before_duplicates.next is not None and node_before_duplicates.next.value == val:
                node_before_duplicates.next = node_before_duplicates.next.next
                if not all:
                    return
            node = node.next

        self.update_tail()

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
            newNode.next = self.head
            self.head = newNode
        node = self.head
        while node is not None:
            if node is afterNode:
                newNode.next = node.next
                node.next = newNode
                return
            node = node.next
        self.update_tail()

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

    def fill_from_array(self, values):
        for value in values:
            node = Node(value)
            self.add_in_tail(node)
        return self

    def __str__(self):
        node = self.head
        string = ''
        while node is not None:
            string += f'{node.value}, '
            node = node.next
        return string

