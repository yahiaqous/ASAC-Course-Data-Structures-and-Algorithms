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


# CC07
def test_kth_greater_than_the_length_of_the_linked_list():
    actual = list.kth(10)
    expected = "Input is greater than the length of the linked list"
    assert actual == expected

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

