class Node:
  def __init__(self, value, left=None, right=None):
    self.value = value
    self.left = left
    self.right = right

class BinaryTree:
  def __init__(self, root=None):
    self.root = root

  def pre_order(self, values=[]):
    def walk(input_node, value_list):
      if not input_node:
        return
      value_list.append(input_node.value)
      walk(input_node.left, value_list)
      walk(input_node.right, value_list)
    walk(self.root, values)
    return values

  def in_order(self, values=[]):
    def walk(input_node, value_list):
      if not input_node:
        return
      walk(input_node.left, value_list)
      value_list.append(input_node.value)
      walk(input_node.right, value_list)
    walk(self.root, values)
    return values

  def post_order(self, values=[]):
    def walk(input_node, value_list):
      if not input_node:
        return
      walk(input_node.left, value_list)
      walk(input_node.right, value_list)
      value_list.append(input_node.value)
    walk(self.root, values)
    return values

# Write the following method for the Binary Tree class
# find maximum value
# Arguments: none
# Returns: number
# Find the maximum value stored in the tree. You can assume that the values stored in the Binary Tree will be numeric.
  def find_maximum_value(self):
    if not self.root:
      return None
    def walk(input_node, max_value):
      if not input_node:
        return max_value
      if input_node.value > max_value:
        max_value = input_node.value
      max_value = walk(input_node.left, max_value)
      max_value = walk(input_node.right, max_value)
      return max_value
    return walk(self.root, self.root.value)
