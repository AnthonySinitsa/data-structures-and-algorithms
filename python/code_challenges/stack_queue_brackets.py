from data_structures.stack import Stack

def multi_bracket_validation(str):
  #create instance of stack used for storing brackets
  stack = Stack()
  left_brackets = ['(', '[', '{']
  right_brackets = [')', ']', '}']

  for i in str:
    if i in left_brackets:
      stack.push(i)
    elif i in right_brackets:
      if stack.is_empty():
        return False
      #check if the right bracket matches the left bracket
      if i == ')' and stack.peek() == '(':
      #if it does, pop the left bracket off the stack
        stack.pop()
      elif i == ']' and stack.peek() == '[':
        stack.pop()
      elif i == '}' and stack.peek() == '{':
        stack.pop()
      else:
        return False
  if stack.is_empty():
    return True
  else:
    return False
