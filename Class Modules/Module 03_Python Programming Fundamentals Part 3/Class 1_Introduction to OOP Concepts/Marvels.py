# Class definition (blueprint)
class Avenger:
    pass  # We'll fill this later



# Creating a Class & Object
class Avenger:
    def fight(self):
        print("Avenger is fighting!")

# Create objects
ironman = Avenger()
hulk = Avenger()

ironman.fight()
hulk.fight()



# Introducing Methods
class Avenger:
    def introduce(self, name):
        print(f"I am {name}, and I protect the world!")

ironman = Avenger()
ironman.introduce("Iron Man")


# Default Constructor​
class Avenger:
    def __init__(self):
        print("A new Avenger has joined the team!")

captain = Avenger()


# Parameterized Constructor
class Avenger:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def show(self):
        print(f"{self.name} has power: {self.power}")

spiderman = Avenger("Spider-Man", "Web-Slinging")
spiderman.show()



# pass statement
class BlackWidow:
    pass  # To be developed in next update



# Intro to Inheritance
class Hero:
    def protect(self):
        print("Protecting the Earth!")

class IronMan(Hero):
    def fly(self):
        print("Flying in the suit!")

tony = IronMan()
tony.protect()  # Inherited
tony.fly()      # Own method




