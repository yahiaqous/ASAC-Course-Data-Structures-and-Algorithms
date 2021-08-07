class Node:
    def __init__(self,value=""):
        self.value=value
        self.next = None
    def __str__(self):
        return str(self.value)


class LinkedList():
    def __init__(self):
        self.head = None

    def __str__(self):
        current = self.head
        string = ''

        while current:
            string+=str(current)+' -> '
            current=current.next
        string+="None"
        return string

#CC05
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


# CC06
    def append(self,new_value):
        node = Node(new_value)
        current=self.head
        if current:
            while current.next:
                current = current.next
            current.next = node
        else:
            self.head = node

    def insert_before(self,value, new_value):
        node = Node(new_value)
        current = self.head
        prev =self.head

        while current:
            if current.value == value:
                if current==prev:
                    self.head = node
                    node.next = current
                    break
                else:
                    prev.next = node
                    node.next = current
            prev = current
            current = current.next

    def insert_after(self,value, new_value):
        node = Node(new_value)
        current = self.head

        while current:
            if current.value == value:
                node.next = current.next
                current.next = node
                break
            current=current.next


# CC07
    def kth(self,number):
        current = self.head
        list_length=1
        while current.next:
            list_length+=1
            current=current.next
        current=self.head

        if number > list_length:
            return("Input is greater than the length of the linked list")
        elif number < 0:
            return("Input k is not a positive integer")
        target = list_length - number - 1

        for i in range(list_length):
            if i == target:
                return(current.value)
            else:
                current=current.next


# CC08
    def zip_lists(self,list1,list2):
        output_list=LinkedList()
        current1 = list1.head
        current2 = list2.head

        while current1 and current2  :
            output_list.append(current1)
            output_list.append(current2)
            current1 = current1.next
            current2 = current2.next

        while current1:
            output_list.append(current1)
            current1 = current1.next
        while current2:
            output_list.append(current2)
            current2 = current2.next

        return output_list


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
    # print(linked_list)
    # print(linked_list.includes(7))

# CC06
    linked_list.append(7)
    # print(linked_list)
    linked_list.append(11)
    linked_list.append(13)
    linked_list.insert_before(5,8)
    print(linked_list)
    linked_list.insert_before(6,5)
    print(linked_list)
    linked_list.insert_before(5,19)
    print(linked_list)
    linked_list.insert_after(3,12)
    linked_list.insert_after(13,9)
    print(linked_list)

# CC07
    print(linked_list.kth(16))
    print(linked_list.kth(14))
    print(linked_list.kth(-5))

# CC08
    linked_list1=LinkedList()
    linked_list2=LinkedList()
    linked_list1.head = node5
    linked_list2.head = node3
    print(linked_list1)
    print(linked_list2)
    linked_list3= LinkedList()
    linked_list3=linked_list3.zip_lists(linked_list1,linked_list2)
    print(linked_list3)

