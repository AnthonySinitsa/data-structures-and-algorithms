from data_structures.hashtable import Hashtable

# Write a function called repeated word that finds the first word to occur more than once in a string
# Arguments: string
# Return: string
def first_repeated_word(string):
  """_summary_

  Args:
      string (_type_): _description_

  Returns:
      _type_: _description_
  """
  # create a hashtable
  hashtable = Hashtable()
  # split the string into an array of words
  words = string.split()
  words = [word.lower().strip(",.?!") for word in words]
  # iterate over the words
  for word in words:
    # if the word is in the hashtable
    if hashtable.contains(word):
      # return the word
      return word
    else:
      # add the word to the hashtable
      hashtable.set(word, word)
  return None

#time complexity: O(n)
#space complexity: O(n)
