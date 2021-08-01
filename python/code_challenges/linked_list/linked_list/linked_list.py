class Node:
    def __init__(self,value=""):
        self.value=value
        self.next = None
    def __str__(self):
        return str(self.value)

class LinkedList():

    def __init__(self):
        self.head = None
    def insert(self, value):
        node = Node(value)
        if self.head:
            node.next=self.head
        self.head = node

    def some_method(self):
        pass

    def __str__(self):
        return str(self.head)

if __name__ == "__main__":
    first_instant = LinkedList('hello')
    print (str(first_instant))
    print(first_instant.next)
