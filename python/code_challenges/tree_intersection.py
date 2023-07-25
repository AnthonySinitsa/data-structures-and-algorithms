from data_structures.binary_tree import BinaryTree

# Write a function called tree_intersection that takes two binary trees as parameters.
# Using your Hashmap implementation as a part of your algorithm, return a set of values found in both trees.
def tree_intersection(tree_a, tree_b):
  # create a set to store the values found in both trees
  set_of_values = set()
  # create a hashmap to store the values of tree_a
  hashmap = {}
  # traverse tree_a and add the values to the hashmap
  def traverse_a(node):
    if node:
      # add the value to the hashmap
      hashmap[node.value] = node.value
      # traverse the left and right nodes
      traverse_a(node.left)
      traverse_a(node.right)
  traverse_a(tree_a.root)
  # traverse tree_b and check if the value is in the hashmap
  def traverse_b(node):
    if node:
      if node.value in hashmap:
        # if the value is in the hashmap, add it to the set
        set_of_values.add(node.value)
      traverse_b(node.left)
      traverse_b(node.right)
  traverse_b(tree_b.root)
  # return the set of values
  return set_of_values

#time complexity: O(n)
#because we are traversing each node in the tree once
#space complexity: O(n)
#because we are creating a hashmap and a set that will store the values of the tree
