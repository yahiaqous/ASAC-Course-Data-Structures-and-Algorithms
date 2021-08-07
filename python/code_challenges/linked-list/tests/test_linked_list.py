import pytest
from linked_list.linked_list import LinkedList, Node


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

