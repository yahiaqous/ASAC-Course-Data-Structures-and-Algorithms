import pytest
from linked_list.linked_list import LinkedList


def test_import():
    assert LinkedList


def test_insert():
    linked_list = LinkedList()
    with pytest.raises(AttributeError):
        linked_list.head.value
    linked_list.insert("first")
    actual = linked_list.head.value
    assert actual == "first"
