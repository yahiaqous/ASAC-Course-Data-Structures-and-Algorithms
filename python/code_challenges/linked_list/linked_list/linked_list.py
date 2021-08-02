class Node:
    def __init__(self,value=""):
        self.value=value
        self.next = None
    def __str__(self):
        return str(self.value)

class LinkedList():
    def __init__(self):
        self.head = None

    # CC05
    def insert(self, value):
        node = Node(value)
        if self.head:
            node.next=self.head
        self.head = node

    def some_method(self):
        pass

    def __str__(self):
        return str(self.head)


    # CC06
    # We stuck here for more then two hours
    def append(self,value=''):
        print(value)
        node = Node(value)
        current = self.head

        while current.next != None:
            current = current.next
        current.next = node

    def insert_before(self,value, new_value):
        pass

    def insert_after():
        pass

if __name__ == "__main__":
    # CC05
    first_instant = LinkedList('hello')
    print (str(first_instant))
    print(first_instant.next)

    # CC06
    new = LinkedList()
    new.append(3)
    print(new)

