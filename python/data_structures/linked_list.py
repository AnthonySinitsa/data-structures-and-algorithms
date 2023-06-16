class Node:
  def __init__(self, value, _next=None):
    self.value = value
    self.next = _next

class LinkedList:
  def __init__(self, head=None):
    self.head = None
  def insert(self, value):
    self.head = Node(value, self.head)
  # check if linkedlist is empty
  def __str__(self):
    if self.head == None:
      return "NULL"
    else:
      current = self.head
      output = ""
      while current:
        output += f"{{ {current.value} }} -> "
        current = current.next
      output += "NULL"
      return output
  def includes(self, value):
    current = self.head
    while current:
      if current.value == value:
        return True
      current = current.next
    return False




# class TargetError:
#   pass


#Create a Linked List class
#Within your Linked List class, include a head property.
#Upon instantiation, an empty Linked List should be created.
#The class should contain the following methods insert
#Arguments: value
#Returns: nothing
#Adds a new node with that value to the head of the list with an O(1) Time performance. includes
#Arguments: value
#Returns: Boolean
#Indicates whether that value exists as a Node’s value somewhere within the list. to string
#Arguments: none
#Returns: a string representing all the values in the Linked List, formatted as: "{ a } -> { b } -> { c } -> NULL"
