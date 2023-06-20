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

class TargetError:
  pass
