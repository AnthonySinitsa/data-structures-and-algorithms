from data_structures.invalid_operation_error import InvalidOperationError

class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


class Stack:
  def __init__(self, node=None):
    self.top = node

  def push(self, value):
    new_node = Node(value)# create a new node
    new_node.next = self.top# set the new node's next to the current top
    self.top = new_node# set the new node to the top

  def pop(self):
    if self.top is None:# if the top is none, raise an error
      raise InvalidOperationError("Method not allowed on empty collection")# raise an error
    value = self.top.value# set the value to the top's value
    self.top = self.top.next#
    return value

  def peek(self):
    if self.top is None:# if the top is none, raise an error
      raise InvalidOperationError("Method not allowed on empty collection")# raise an error
    return self.top.value# return the top's value

  def is_empty(self):
    return self.top is None# return true if the top is none, else return false
