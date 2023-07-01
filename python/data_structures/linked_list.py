class Node:
    def __init__(self, value, _next=None):
        self.value = value
        self._next = _next

class LinkedList:
  def __init__(self, head=None, values=None, insert=None):
    self.head = None

  def insert (self, value):
    newNode = Node(value)
    newNode._next = self.head
    self.head = newNode

  def append(self, value):
    newNode = Node(value)
    if self.head is None:
      self.head = newNode
    else:
      current = self.head
      while current._next is not None:
        current = current._next
      current._next = newNode

  def insert_before(self, value, new_value):
      current = self.head
      previous = None
      if current is None:
        raise ValueError(f"Value {value} not found in linked list")

      while current is not None and current.value != value:
        previous = current
        current = current._next

      if current is None:
        raise ValueError(f"Value {value} not found in linked list")

      newNode = Node(new_value)
      newNode._next = current
      if previous is None:
        self.head = newNode
      else:
        previous._next = newNode

  def insert_after(self, value, new_value):
      current = self.head
      while current is not None and current.value != value:
        current = current._next

      if current is None:
        raise ValueError(f"Value {value} not found in linked list")
      newNode = Node(new_value)
      newNode._next = current._next
      current._next = newNode

  def __str__(self):
    if self.head == None:
      return "NULL"
    else:
      current = self.head
    output = ""
    while current:
      output += f"{{ {current.value} }} -> "
      current = current._next
    output += "NULL"
    return output

  def includes(self, value):
    current = self.head
    while current:
      if current.value == value:
          return True
      current = current._next
    return False

  #kth from end
  #argument: a number, k, as a parameter.
  #Return the node’s value that is k places from the tail of the linked list.
  #You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.
  def kth_from_end(self, k):
    current = self.head
    count = 0
    while current:
      count += 1
      current = current._next
    if k < 0 or k >= count:
      raise TargetError("Target not found")
    current = self.head
    for i in range(count - k - 1):
      current = current._next
    return current.value

  # Write a function called zip lists
  # Arguments: 2 linked lists
  # Return: New Linked List
  # Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the the zipped list.
  @staticmethod
  def zip_lists(list1, list2):
    current1 = list1.head
    current2 = list2.head
    if current1 == None:
      return list2
    if current2 == None:
      return list1
    while current1 and current2:
      temp1 = current1._next
      temp2 = current2._next
      current1._next = current2
      current2._next = temp1
      current1 = temp1
      current2 = temp2
    return list1

#create a TargerError class that doesn't pass
class TargetError(Exception):
  def __init__(self, message):
    self.message = message
