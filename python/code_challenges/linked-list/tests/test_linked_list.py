import pytest
from linked_list.linked_list import LinkedList, Node

# CC05
def test_import():
    assert LinkedList

def test_instantiate_empty_list():
    linked_list=LinkedList()
    assert linked_list

def test_insert():
    linked_list = LinkedList()
    linked_list.insert("first")
    actual = linked_list.head.value
    assert actual == "first"

def test_head():
    node1=Node(5)
    linked_list = LinkedList()
    linked_list.head=node1
    assert linked_list.head == node1

def test_insert_multiple_nodes():
    node1=Node(1)
    linked_list = LinkedList()
    linked_list.head=node1
    linked_list.insert(4)
    assert linked_list.head.value == 4
    linked_list.insert(6)
    assert linked_list.head.value == 6
    linked_list.insert(9)
    assert linked_list.head.value == 9

def test_includes():
    node1=Node(1)
    node2=Node(2)
    node3=Node(3)
    node4=Node(4)
    linked_list = LinkedList()
    linked_list.head=node1
    node1.next=node2
    node2.next=node3
    node3.next=node4
    assert linked_list.includes(1)
    assert linked_list.includes(2)
    assert linked_list.includes(3)
    assert linked_list.includes(4)
    assert linked_list.includes(5)==False
    assert linked_list.includes(6)==False

def test_values_exist_in_the_linked_list():
    node1=Node(1)
    node2=Node(2)
    node3=Node(3)
    node4=Node(4)
    linked_list = LinkedList()
    linked_list.head=node1
    node1.next=node2
    node2.next=node3
    node3.next=node4
    assert linked_list.__str__() == "1 -> 2 -> 3 -> 4 -> None"


# CC06
def test_add__node_to_the_end_of_the_linked_list():
    node1=Node(1)
    node2=Node(2)
    node3=Node(3)
    node4=Node(4)
    linked_list = LinkedList()
    linked_list.head=node1
    node1.next=node2
    node2.next=node3
    node3.next=node4
    linked_list.append(5)
    assert linked_list.__str__() == "1 -> 2 -> 3 -> 4 -> 5 -> None"

def test_add_multiple_nodes_to_the_end_of_linked_list():
    node1=Node(1)
    node2=Node(2)
    node3=Node(3)
    node4=Node(4)
    linked_list = LinkedList()
    linked_list.head=node1
    node1.next=node2
    node2.next=node3
    node3.next=node4
    linked_list.append(5)
    linked_list.append(6)
    linked_list.append(7)
    assert linked_list.__str__() == "1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> None"

def test_insert_node_before_node_located_in_the_middle_of_linked_list():
    node1=Node(1)
    node2=Node(2)
    node3=Node(3)
    node4=Node(4)
    linked_list = LinkedList()
    linked_list.head=node1
    node1.next=node2
    node2.next=node3
    node3.next=node4
    linked_list.insert_before(3,5)
    assert linked_list.__str__() == "1 -> 2 -> 5 -> 3 -> 4 -> None"

def test_insert_node_before_the_first_node():
    node1=Node(1)
    node2=Node(2)
    node3=Node(3)
    node4=Node(4)
    linked_list = LinkedList()
    linked_list.head=node1
    node1.next=node2
    node2.next=node3
    node3.next=node4
    linked_list.insert_before(1,5)
    assert linked_list.__str__() == "5 -> 1 -> 2 -> 3 -> 4 -> None"

def test_insert_after_node_located_in_the_middle_of_linked_list():
    node1=Node(1)
    node2=Node(2)
    node3=Node(3)
    node4=Node(4)
    linked_list = LinkedList()
    linked_list.head=node1
    node1.next=node2
    node2.next=node3
    node3.next=node4
    linked_list.insert_after(2,5)
    assert linked_list.__str__() == "1 -> 2 -> 5 -> 3 -> 4 -> None"

def test_insert_node_after_the_last_node():
    node1=Node(1)
    node2=Node(2)
    node3=Node(3)
    node4=Node(4)
    linked_list = LinkedList()
    linked_list.head=node1
    node1.next=node2
    node2.next=node3
    node3.next=node4
    linked_list.insert_after(4,5)
    assert linked_list.__str__() == "1 -> 2 -> 3 -> 4 -> 5 -> None"


# CC07
# def test_kth_greater_than_the_length_of_the_linked_list():
#     actual = list.kth(10)
#     expected = "Input is greater than the length of the linked list"
#     assert actual == expected

# def test_k_same_length_as_list():
#     actual = list.kth(7)
#     expected = 1
#     assert actual == expected

# def test_k_is_not_postive_integer():
#     actual = list.kth(-3)
#     expected = "Input k is not a positive integer"
#     assert actual == expected

# def test_linked_list_size_1():
#     alone_node = Node(5)
#     linked_list=LinkedList()
#     linked_list.head = alone_node

#     actual = linked_list.kth(0)
#     expected = 5
#     assert actual == expected
