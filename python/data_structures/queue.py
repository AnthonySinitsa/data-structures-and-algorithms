from data_structures.invalid_operation_error import InvalidOperationError

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next

class Queue:

  def __init__(self, node=None):
    self.front = node# set the front to the node
    self.rear = node# set the rear to the node

  def enqueue(self, value):
    new_node = Node(value)# create a new node
    if self.rear:# if the rear exists
      self.rear.next = new_node# set the rear's next to the new node
    else:
      self.front = new_node# set the front to the new node
    self.rear = new_node# set the rear to the new node

  def dequeue(self):
    if self.front is None:# if the front is none, raise an error
      raise InvalidOperationError("Method not allowed on empty collection")#raise an error
    dequeued = self.front.value# set the dequeued to the front's value
    self.front = self.front.next# set the front to the front's next
    if self.front is None:# if the front is none
      self.rear = None# set the rear to none
    return dequeued# return the dequeued

  def peek(self):
    if self.front is None:# if the front is none, raise an error
      raise InvalidOperationError("Method not allowed on empty collection")# raise an error
    return self.front.value# return the front's value

  def is_empty(self):
    return self.front is None# return true if the front is none, else return false
