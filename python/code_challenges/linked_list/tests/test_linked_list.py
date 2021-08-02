import pytest
from linked_list.linked_list import LinkedList


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

