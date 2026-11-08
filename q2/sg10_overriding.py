# create parent class Animal
class Animal:

  # initialize the name attribute of the animal
  def __init__(self, name):
    self.name = name

  # define method for making sound
  def make_sound(self):
    print(f"{self.name} makes a sound.")

  # define method for eating
  def eat(self):
    print(f"{self.name} eats food.")

# create child class Lion that inherits from parent class Animal
class Lion(Animal):

  # override the parent's make_sound() method
  def make_sound(self):
    print(f"{self.name} roars loudly!")

  # override the parent's eat() method
  def eat(self):
    print(f"{self.name} eats fresh meat.")

# create child class Elephant that inherits from parent class Animal
class Elephant(Animal):

  # override the parent's make_sound() method
  def make_sound(self):
    print(f"{self.name} trumpets!")

  # override the parent's eat() method
  def eat(self):
    print(f"{self.name} eats grass and fruits.")

# create child class Monkey that inherits from parent class Animal
class Monkey(Animal):

  # override the parent's make_sound() method
  def make_sound(self):
    print(f"{self.name} chatters!")

  # override the parent's eat() method
  def eat(self):
    print(f"{self.name} eats bananas.")

# create an object for each child class
lion = Lion("Simba")
elephant = Elephant("Dumbo")
monkey = Monkey("George")

# store all objects in a list
animals = [lion, elephant, monkey]

# use a for loop to call each child class' methods
for animal in animals:
    animal.make_sound()
    animal.eat()
    print("----")