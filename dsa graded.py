class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements))

    def insert_after(self, target, data):
        current = self.head
        while current:
            if current.data == target:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next

    def delete_head(self):
        if self.head:
            self.head = self.head.next

    def delete_value(self, target):
        current = self.head
        if current and current.data == target:
            self.head = current.next
            return
        prev = None
        while current and current.data != target:
            prev = current
            current = current.next
        if current:
            prev.next = current.next

llist = LinkedList()
for val in [2, 8, 11, 7, 3]:
    llist.append(val)

llist.insert_after(8, 5)
llist.insert_after(3, 15)
llist.delete_head()
llist.delete_value(11)

llist.display()