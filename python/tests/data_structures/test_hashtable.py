import pytest
from data_structures.hashtable import Hashtable


def test_exists():
    assert Hashtable


# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


@pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item:
            actual.append(item.display())

    expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

    assert actual == expected

def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")
    # not sure where .dispaly is supposed to, keys method get keys from  Hashtable.
    actual = hashtable.keys()
    expected = ["ahmad", "silent", "listen"]
    assert set(actual) == set(expected)

# Setting a key/value to your hashtable results in the value being in the data structure
# Retrieving based on a key returns the value stored
# Successfully returns null for a key that does not exist in the hashtable
# Successfully returns a list of all unique keys that exist in the hashtable
# Successfully handle a collision within the hashtable
# Successfully retrieve a value from a bucket within the hashtable that has a collision
# Successfully hash a key to an in-range value

def test_hash():
    hashtable = Hashtable()
    actual = hashtable.hash("apple")
    expected = 854
    assert actual == expected

def test_keys():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    hashtable.set("banana", "Used for banana bread")
    hashtable.set("orange", "Used for orange juice")
    actual = hashtable.keys()
    expected = ["apple", "banana", "orange"]
    assert set(actual) == set(expected)
