class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insertfromlast(self, val):
        temp = Node(val)

        if self.size == 0:
            self.head = temp
            self.tail = temp
            self.size += 1
        else:
            self.tail.next = temp
            self.tail = temp
            self.size += 1

    def display(self):
        temp = self.head
        print("START --->", end="")
        while temp is not None:
            print(f"{temp.value}--->", end="")
            temp = temp.next
        print("end")

    def insert(self, value, index):
        temp = self.head
        for _ in range(index - 1):
            temp = temp.next

        newtemp = Node(value, temp.next)
        temp.next = newtemp

    def deletefirst(self):
        if self.head is not None:
            self.head = self.head.next

    def deleteNode(self, targetValue):
        if self.head is None:
            return

        if self.head.value == targetValue:
            self.head = self.head.next
            return

        current = self.head

        while current.next is not None and current.next.value != targetValue:
            current = current.next

        if current.next is not None:
            current.next = current.next.next
        else:
            print(f"Value {targetValue} not found in the list.")

if __name__ == "__main__":
    l1 = linkedlist()
    l1.insertfromlast(2)
    l1.insertfromlast(8)
    l1.insertfromlast(11)
    l1.insertfromlast(7)
    l1.insertfromlast(3)

    l1.display()

    l1.insert(5, 3)
    l1.display()

    l1.insertfromlast(15)
    l1.display()

    l1.deletefirst()
    l1.display()

    l1.deleteNode(11)
    l1.display()