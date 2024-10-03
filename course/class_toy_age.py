class Aging_toy:
    def __init__(self, name, color) :
        self.name = name
        self.color = color
        self.age = 0 # attribute having a default value
    
    def color_print(self):
        """toy's color"""
        your_color = f"{self.name} is {self.color}"
        return your_color

    def age_print(self):
        """toy's age"""
        print(f"{self.name} is {self.age} years old")

    def set_age(self,new_age):
        """update toy's age"""
        self.age = new_age

    def increase_age(self,increase):
        """increase toy's age"""
        self.age += increase

alice_toy = Aging_toy('woody','yellow')
bob_toy = Aging_toy('buzz','violet')

# toys get older
#1 directly access attributes' values
alice_toy.age_print()
alice_toy.age = 20
alice_toy.age_print()

#2 create a method to update a value ~ setter in java
bob_toy.age_print()
bob_toy.set_age(1000)
bob_toy.age_print()

#3 create a method to increase a value
bob_toy.increase_age(20)
bob_toy.age_print()

# in a broad sense, you can either use a method or access a field to change its value



