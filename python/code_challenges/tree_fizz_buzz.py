from data_structures.binary_tree import BinaryTree
from data_structures.kary_tree import KaryTree, Node

def fizz_buzz_tree(tree):
  # if tree is empty, return empty tree
  if not tree or not tree.root:
    return KaryTree()
  # create new tree
  new_tree = KaryTree(Node())
  # traverse tree, adding fizzbuzz values to new tree
  def traverse(node, new_node):
    # if node is divisible by 3 and 5, set value to "FizzBuzz"
    if node.value % 3 == 0 and node.value % 5 == 0:
      new_node.value = "FizzBuzz"
    # if node is divisible by 3, set value to "Fizz"
    elif node.value % 3 == 0:
      new_node.value = "Fizz"
    # if node is divisible by 5, set value to "Buzz"
    elif node.value % 5 == 0:
      new_node.value = "Buzz"
    else:
      # else, set value to string of node value
      new_node.value = str(node.value)
    # if node has children, traverse them
    for child in node.children:
      # create new child node
      new_child = Node()
      # add new child to new node's children
      new_node.children.append(new_child)
      # traverse child node
      traverse(child, new_child)
  # traverse tree
  traverse(tree.root, new_tree.root)
  return new_tree
