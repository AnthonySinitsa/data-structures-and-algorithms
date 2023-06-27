from data_structures.queue import Queue

#the animal shelter class has two queues, one for dogs and one for cats. when you enqueue an animal, it checks if it's a dog or a cat and puts it in the appropriate queue. when you dequeue, it checks if the pref is a dog or a cat and returns the first animal in that queue. if the pref is neither a dog nor a cat, it returns None.

class Animal:
  def __init__(self, species, name):
    self.species = species
    self.name = name


class Dog(Animal):
  def __init__(self, name=""):
    super().__init__("dog", name)
    #super() calls the parent class's constructor and add to it.


class Cat(Animal):
  def __init__(self, name=""):
    super().__init__("cat", name)


class AnimalShelter:
  def __init__(self):
    self.dogs = Queue()
    self.cats = Queue()

  def enqueue(self, animal):
    if animal.species == "dog":
      self.dogs.enqueue(animal)
    elif animal.species == "cat":
      self.cats.enqueue(animal)
    else:
      return "Sorry, we only accept cats and dogs."

  def dequeue(self, pref):
    if pref == "dog":
      return self.dogs.dequeue()
    elif pref == "cat":
      return self.cats.dequeue()
    else:
      return None
