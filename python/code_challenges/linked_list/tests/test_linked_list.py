import pytest
from linked_list.linked_list import LinkedList,Node

node1 = Node(1)
node2 = Node(2)
node3 = Node(6)
node4 = Node(4)
node5 = Node(9)
node6 = Node(25)
node7 = Node(14)
node8 = Node(3)

list = LinkedList()
list.head = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8

# CC05
def test_import():
    assert LinkedList

def test_insert():
    linked_list = LinkedList()
    with pytest.raises(AttributeError):
        linked_list.head.value
    linked_list.insert("first")
    actual = linked_list.head.value
    assert actual == "first"

# CC06
# def test_add__node_to_the_end_of_the_linked_list():
#     assert LinkedList.append()

# def add_multiple_nodes_to_the_end_of_linked_list():
#     value1 = 5
#     value2 = 10
#     assert LinkedList.append(value1) == 5
#     assert LinkedList.append(value2) == 10

# def insert_node_before_node_located_i_the_middle_of_linked_list():
#     value = 5
#     new_value = 10
#     assert LinkedList.insert_before(value,new_value) ==

# CC07
def test_kth_greater_than_the_length_of_the_linked_list():
    actual = list.kth(10)
    expected = "Input is greater than the length of the linked list"
    assert actual == expected



#Where k and the length of the list are the same
def test_k_same_length_as_list():
    actual = list.kth(7)
    expected = 1
    assert actual == expected

def test_k_is_not_postive_integer():
    actual = list.kth(-3)
    expected = "Input k is not a positive integer"
    assert actual == expected

def test_linked_list_size_1():
    alone_node = Node(5)
    linked_list=LinkedList()
    linked_list.head = alone_node

    actual = linked_list.kth(0)
    expected = 5
    assert actual == expected

