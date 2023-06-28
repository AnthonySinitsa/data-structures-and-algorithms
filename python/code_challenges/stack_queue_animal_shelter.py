from data_structures.queue import Queue

class Dog:
  def __init__(self):
    self.species = "dog"
    self.name = "dog"

class Cat:
  def __init__(self):
    self.species = "cat"
    self.name = "cat"

class AnimalShelter:
  def __init__(self):
    self.queue = Queue()

  def enqueue(self, animal):
    self.queue.enqueue(animal)

  def dequeue(self, pref):
    if pref != "dog" and pref != "cat":
      return None
    else:
      while self.queue.front:
        if self.queue.front.value.species == pref:
          return self.queue.dequeue()
        else:
          self.queue.enqueue(self.queue.dequeue())
      return None
