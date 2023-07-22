class Hashtable:
  """
  This is a Hashtable class
  Paramaters: Key, Value
  Returns: Hashtable
  """
  #explain this code to me

  def __init__(self, size=1024):
    self._size = size
    self._buckets = [[] for i in range(size)]
    #create a list of lists, and we want to create a list of lists that is the size of the size that is passed in.

  def hash(self, key):
    """
    This is a hash function
    Paramaters: Key
    Returns: Index
    """
    total = 0
    for char in key:
      total += ord(char)
      # ord() function returns an integer representing the Unicode character.
    primed = total * 19
    index = primed % self._size
    # % is the modulo operator, which returns the remainder of dividing the left operand by the right operand.
    return index

  # The get() method takes in a key, gets the Hash, and goes to the index location specified. Once at the index location is found in the array, it is then the responsibility of the algorithm the iterate through the bucket and see if the key exists and return the value.
  def get(self, key):
    """
    This is a get function
    Paramaters: Key
    Returns: Value
    """
    index = self.hash(key)#hashes key
    for item in self._buckets[index]:
      #iterates through the bucket
      if item[0] == key:
        #checks if the key is equal to the key passed in
        return item[1]
      #returns the value
    return None



# set
# Arguments: key, value
# Returns: nothing
# This method should hash the key, and set the key and value pair in the table, handling collisions as needed.
# Should a given key already exist, replace its value from the value argument given to this method.
  def set(self, key, value):
    index = self.hash(key)#hashes key
    for item in self._buckets[index]:
      #iterates through the bucket
      if item[0] == key:
        #checks if the key is equal to the key passed in
        item[1] = value
        #sets the value to the value passed in
        return
      #returns the value
    self._buckets[index].append((key, value))
    #appends the key and value to the bucket

# The has() method will accept a key, and return a bool on if that key exists inside the hashtable. The best way to do this is to have the contains call the hash() method and check the hashtable if the key exists in the table given the index returned.

  def has(self, key):
    """
    This is a has function
    Paramaters: Key
    Returns: Boolean
    """
    index = self.hash(key)#hashes key
    for item in self._buckets[index]:
      #iterates through the bucket
      if item[0] == key:
        #checks if the key is equal to the key passed in
        return True#if so return true
    return False#else return false

# The keys() method returns a collection (array) of unique hash keys.
  def keys(self):
    """
    This is a keys function
    Paramaters: None
    Returns: Array
    """
    keys = []
    for bucket in self._buckets:
      #iterates through the buckets
      for item in bucket:
        #iterates through the bucket
        keys.append(item[0])
        #appends the key to the keys array
    return keys

  def display(self):
    """
    This is a display function
    Paramaters: None
    Returns: Array
    """
    for bucket in self._buckets:
      #iterates through the buckets
      if bucket:
        #checks if the bucket is not empty
        print(bucket)
        #prints the bucket
