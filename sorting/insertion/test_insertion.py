import pytest
from insertion import insertion_sort

def test_insertion_sort_empty_list():
  arr = []
  assert insertion_sort(arr) == []

def test_insertion_sort_single_element():
  arr = [5]
  assert insertion_sort(arr) == [5]

def test_insertion_sort():
  arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
  assert insertion_sort(arr) == [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]

def test_insertion_sort_negative_numbers():
  arr = [5, -3, 0, -7, 2, -1]
  assert insertion_sort(arr) == [-7, -3, -1, 0, 2, 5]

def test_assignment_values():
  arr = [8,4,23,42,16,15]
  assert insertion_sort(arr) == [4, 8, 15, 16, 23, 42]
