# can be done with one function
def insertion_sort(arr): # takes in an array
  for i in range(1, len(arr)): # for loop to iterate through the array
    value = arr[i] # value is the current element
    j = i - 1 # j is the previous element
    while j >= 0 and arr[j] > value: # while loop to check if the previous element is greater than the current element
      arr[j + 1] = arr[j] # if it is, then the previous element is moved to the next element
      j -= 1 # j is decremented
    arr[j + 1] = value # the current element is moved to the next element
  return arr # return the sorted array

# time complexity: O(n^2) because of the nested while loop
# space complexity: O(1) because the array is sorted in place
