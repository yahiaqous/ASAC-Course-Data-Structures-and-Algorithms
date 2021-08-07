#CC05
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

    def includes(self,value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def __str__(self):
        current = self.head
        string = ''

        while current:
            string+=str(current)+' -> '
            current=current.next
        string+="None"
        return string


if __name__ == "__main__":

#CC05
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    linked_list = LinkedList()
    linked_list.head = node1
    node1.next=node2
    node2.next=node3
    node3.next=node4
    node4.next=node5
    linked_list.insert(6)
    print(linked_list)
    print(linked_list.includes(7))

