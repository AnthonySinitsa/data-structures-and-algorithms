from data_structures.binary_tree import BinaryTree

# Write a function called breadth first
# Arguments: tree
# Return: list of all values in the tree, in the order they were encountered

def breadth_first(tree):
  if tree.root is None:
    return []
  queue = []
  queue.append(tree.root)
  result = []
  while len(queue) > 0:#while queue is not empty
    current = queue.pop(0)#remove first item from queue
    result.append(current.value)#add current value to result
    if current.left:#if current has a left child
      queue.append(current.left)#add left child to queue
    if current.right:#if current has a right child
      queue.append(current.right)#add right child to queue
  return result
