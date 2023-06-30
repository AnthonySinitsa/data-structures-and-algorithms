from data_structures.binary_tree import BinaryTree
from data_structures.binary_tree import Node

class BinarySearchTree(BinaryTree):
  def __init__(self, root=None):
    super().__init__(root)

  def add(self, value):
    if not self.root:
      # if there is no root, create one
      self.root = Node(value)
      return
    # if there is a root, traverse the tree
    current = self.root
    while True:
      # if the value is less than the current node, go left
      if value < current.value:
        # if there is no left, create one
        if not current.left:
          current.left = Node(value)
          break
        # if there is a left, go left
        current = current.left
      else:
        # if there is no right, create one
        if not current.right:
          current.right = Node(value)
          break
        # if there is a right, go right
        current = current.right

  def contains(self, value):
    # if there is no root, return False
    if not self.root:
      return False
    # if there is a root, traverse the tree
    current = self.root
    # while there is a current node
    while current:
      # if the value is equal to the current node, return True
      if value == current.value:
        return True
      # if the value is less than the current node, go left
      if value < current.value:
        # if there is no left, return False
        current = current.left
      else:
        # if there is no right, return False
        current = current.right
    return False
