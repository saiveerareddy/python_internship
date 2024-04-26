class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def search(self, key):
        current = self.head
        position = 0
        found = False  # Flag to track if the key is found

        while current:
            position += 1
            if current.data == key:
                print("Data found at position : ", position)
                found = True
                break
            current = current.next

        if not found:
            print("Data not found")


obj = LinkedList()
obj.insert(5)
obj.insert(6)
obj.insert(7)
obj.display()
obj.search(6)
