import pytest
from code_challenges.stack_queue_animal_shelter import AnimalShelter, Dog, Cat


# @pytest.mark.skip("TODO")
def test_single_cat():
    shelter = AnimalShelter()
    cat = Cat()
    shelter.enqueue(cat)
    actual = shelter.dequeue("cat")
    expected = cat
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_single_dog():
    shelter = AnimalShelter()
    dog = Dog()
    shelter.enqueue(dog)
    actual = shelter.dequeue("dog")
    expected = dog
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_dog_preferred_but_cat_in_front():
    shelter = AnimalShelter()
    cat = Cat()
    dog = Dog()
    shelter.enqueue(cat)
    shelter.enqueue(dog)
    actual = shelter.dequeue("dog")
    expected = dog
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_dog_then_cat():
    shelter = AnimalShelter()
    cat = Cat()
    dog = Dog()
    shelter.enqueue(dog)
    shelter.enqueue(cat)
    shelter.dequeue("dog")
    actual = shelter.dequeue("cat")
    expected = cat
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_bad_pref():
    shelter = AnimalShelter()
    cat = Cat()
    dog = Dog()
    shelter.enqueue(dog)
    shelter.enqueue(cat)
    shelter.dequeue("dog")
    actual = shelter.dequeue("lizard")
    expected = None
    assert expected == actual


def test_multiple_cats():
    shelter = AnimalShelter()
    cat = Cat()
    cat2 = Cat()
    cat3 = Cat()
    shelter.enqueue(cat)
    shelter.enqueue(cat2)
    shelter.enqueue(cat3)
    shelter.dequeue("cat")
    actual = shelter.dequeue("cat")
    expected = cat2
    assert actual == expected

def test_multiple_dogs():
    shelter = AnimalShelter()
    dog = Dog()
    dog2 = Dog()
    dog3 = Dog()
    shelter.enqueue(dog)
    shelter.enqueue(dog2)
    shelter.enqueue(dog3)
    shelter.dequeue("dog")
    actual = shelter.dequeue("dog")
    expected = dog2
    assert actual == expected
