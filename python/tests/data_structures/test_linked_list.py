import pytest
from data_structures.linked_list import LinkedList


def test_exists():
    assert LinkedList


# @pytest.mark.skip("TODO")
def test_instantiate():
    assert LinkedList()


# @pytest.mark.skip("TODO")
def test_empty_head():
    linked = LinkedList()
    assert linked.head is None


# @pytest.mark.skip("TODO")
def test_populated_head():
    linked = LinkedList()
    linked.insert("apple")
    assert linked.head.value == "apple"


# @pytest.mark.skip("TODO")
def test_to_string_empty():
    linked_list = LinkedList()

    assert str(linked_list) == "NULL"


# @pytest.mark.skip("TODO")
def test_to_string_single():
    linked_list = LinkedList()

    linked_list.insert("apple")

    assert str(linked_list) == "{ apple } -> NULL"


# @pytest.mark.skip("TODO")
def test_to_string_double():
    linked_list = LinkedList()

    linked_list.insert("apple")

    assert str(linked_list) == "{ apple } -> NULL"

    linked_list.insert("banana")

    assert str(linked_list) == "{ banana } -> { apple } -> NULL"


# @pytest.mark.skip("TODO")
def test_includes_true():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert linked_list.includes("apple")


# @pytest.mark.skip("TODO")
def test_includes_false():
    linked_list = LinkedList()

    linked_list.insert("apple")

    linked_list.insert("banana")

    assert not linked_list.includes("cucumber")


def test_insert():
    linked_list = LinkedList()
    linked_list.insert("apple")
    linked_list.insert("banana")
    linked_list.insert("cucumber")
    assert linked_list.head.value == "cucumber"
    assert linked_list.head.next.value == "banana"
    assert linked_list.head.next.next.value == "apple"
    assert linked_list.head.next.next.next == None



def test_empty_linked_list():
  linked_list = LinkedList()
  assert linked_list.head is None


def test_insert_into_linked_list():
  linked_list = LinkedList()
  linked_list.insert(1)
  assert linked_list.head.value == 1


def test_includes_linked_list():
  linked_list = LinkedList()
  linked_list.insert(1)
  linked_list.insert(2)
  linked_list.insert(3)
  assert linked_list.includes(2) is True
  assert linked_list.includes(4) is False
