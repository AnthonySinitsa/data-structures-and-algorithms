import pytest

from merge import merge_sort

def test_merge_sort():
  # Test with an empty array
  arr = []
  assert merge_sort(arr) == []

  # Test with an array of one element
  arr = [5]
  assert merge_sort(arr) == [5]

  # Test with an already sorted array
  arr = [1, 2, 3, 4, 5]
  assert merge_sort(arr) == [1, 2, 3, 4, 5]

  # Test with an array in descending order
  arr = [5, 4, 3, 2, 1]
  assert merge_sort(arr) == [1, 2, 3, 4, 5]

  # Test with an array containing duplicate elements
  arr = [5, 2, 1, 2, 4, 1]
  assert merge_sort(arr) == [1, 1, 2, 2, 4, 5]

  # Test with a large array
  arr = [9, 5, 2, 7, 1, 6, 8, 3, 10, 4]
  assert merge_sort(arr) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

  # Test with a negative numbers
  arr = [-5, -2, -1, -8, -3]
  assert merge_sort(arr) == [-8, -5, -3, -2, -1]

  # Test with assignment values
  arr = [8, 4, 42, 23, 16, 15]
  assert merge_sort(arr) == [4, 8, 15, 16, 23, 42]
