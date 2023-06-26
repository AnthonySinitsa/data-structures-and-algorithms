import pytest
from code_challenges.stack_queue_pseudo import PseudoQueue


def test_exists():
    assert PseudoQueue


# @pytest.mark.skip("TODO")
def test_enqueue_one():
    pq = PseudoQueue()
    pq.enqueue("apples")
    actual = pq.dequeue()
    expected = "apples"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_enqueue_two():
    pq = PseudoQueue()
    pq.enqueue("apples")
    pq.enqueue("bananas")

    actual = pq.dequeue()
    expected = "apples"
    assert actual == expected

    actual = pq.dequeue()
    expected = "bananas"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_enqueue_dequeue_enqueue_dequeue():
    pq = PseudoQueue()
    pq.enqueue("apples")
    pq.enqueue("bananas")

    pq.dequeue()

    pq.enqueue("cucumbers")
    pq.enqueue("dates")

    actual = [pq.dequeue(), pq.dequeue(), pq.dequeue()]

    expected = ["bananas", "cucumbers", "dates"]

    assert actual == expected
    

def test_dequeue_empty():
    pq = PseudoQueue()
    actual = pq.dequeue()
    expected = 'Queue is empty'
    assert actual == expected

def test_enqueue_dequeue():
    pq = PseudoQueue()
    pq.enqueue("apples")
    pq.enqueue("bananas")
    pq.enqueue("cucumbers")
    pq.enqueue("dates")
    pq.dequeue()
    pq.dequeue()
    pq.dequeue()
    actual = pq.dequeue()
    expected = "dates"
    assert actual == expected
