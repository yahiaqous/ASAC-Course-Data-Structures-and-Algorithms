class Node:
    def __init__(self,value=''):
        self.value = value
        self.next = None



class LinkedList():
    def __init__(self):
        self.head = None

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


if __name__=="__main__":
    new = LinkedList()
    new.append(3)
    print(new)
