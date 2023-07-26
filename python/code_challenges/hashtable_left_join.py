from data_structures.hashtable import Hashtable

# Write a function called left join
# Arguments: two hash maps
# The first parameter is a hashmap that has word strings as keys, and a synonym of the key as values.
# The second parameter is a hashmap that has word strings as keys, and antonyms of the key as values.
# Return: The returned data structure that holds the results is up to you. It doesn’t need to exactly match the output below, so long as it achieves the LEFT JOIN logic
# NOTES:

# Combine the key and corresponding values (if they exist) into a new data structure according to LEFT JOIN logic.
# LEFT JOIN means all the values in the first hashmap are returned, and if values exist in the “right” hashmap, they are appended to the result row.
# If no values exist in the right hashmap, then some flavor of NULL should be appended to the result row.
# Example
# INPUT
# Synonyms Hash Table	 	 	Antonyms Hash Table
# Key	Value	 	Key	Value
# diligent	employed	 	diligent	idle
# fond	enamored	 	fond	averse
# guide	usher	 	guide	follow
# outfit	garb	 	flow	jam
# wrath	anger	 	wrath	delight
# …	…	 	…	…
# OUTPUT
# [
#    ["font", "enamored", "averse"],
#    ["wrath", "anger", "delight"],
#    ["diligent", "employed", "idle"],
#    ["outfit", "garb", 'NONE'],
#    ["guide", "usher","follow"]
# ]

def left_join(synonyms, antonyms):
  results = []
  # Loop through the synonyms
  for word, synonym in synonyms.items():
    # Check if the word is in the antonyms
    if word in antonyms:
      # If it is, append the word, synonym, and antonym to the results
      antonym = antonyms[word]
      # print(word, synonym, antonym)
      results.append([word, synonym, antonym])
      # Remove the word from the antonyms
    else:
      # If it isn't, append the word, synonym, and "NONE" to the results
      results.append([word, synonym, "NONE"])
      # Remove the word from the antonyms
  return results

# time complexity: O(n)
# space complexity: O(n)
