class node:
    def __init__(self,data):
        self.data = data
        self.next=None
class linkedlist:
    def __init__(self):
        self.head = None
    def insert(self,data):
        newnode = node(data)
        if self.head is None:
            self.head = newnode
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newnode
    def display(self):
        current = self.head
        while current:
            print(current.data,end="->")
            current = current.next
    def delete_at_end(self):
        if self.head is None:
            print("The list is empty")
        else:
            current = self.head
            while current.next.next:
                current = current.next
            current.next=None
obj = linkedlist()

obj.insert(5)
obj.insert(6)
obj.insert(6)
obj.delete_at_end(5)
obj.display()


