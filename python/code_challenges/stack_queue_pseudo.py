from data_structures.stack import Stack

# Create a new class called pseudo queue.
# Do not use an existing Queue.
# Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below),
# Internally, utilize 2 Stack instances to create and manage the queue

class PseudoQueue:
  def __init__(self):
    self.stack1 = Stack()
    self.stack2 = Stack()

  def enqueue(self, value):
    self.stack1.push(value)# add to the end of the queue

  def dequeue(self):
    if self.stack1.is_empty():# if the queue is empty, raise an exception
      return 'Queue is empty' # return the value from front of queue
    while not self.stack1.is_empty():# move all the elements from stack1 to stack2
      self.stack2.push(self.stack1.pop())# pop from stack1 and push to stack2
    value = self.stack2.pop()# pop from stack2
    while not self.stack2.is_empty():# move all the elements from stack2 to stack1
      self.stack1.push(self.stack2.pop())# pop from stack2 and push to stack1
    return value# return the value from front of queue
