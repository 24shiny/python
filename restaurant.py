from inheritance import Toy
from random import randint
from random import choice

class Restaurant:
    def __init__(self, name, type) :
        self.name = name
        self.type = type
    
    def describe_rest(self):
        """describe the restaurant"""
        # print(f"{self.name} is a {self.type} restaunrant")
        # alternative way to f-strings
        print("{} is a ".format(self.name), "{} restaurant".format(self.type)) 
    
    def open_rest(self):
        """open the restaurant"""
        print("we are open, welcome!")

class Foodstand(Restaurant): # Wooden_toy extends Toy
    def __init__(self, name, type, menu) :
        """bring parent's attributes"""
        super().__init__(name, type) # call parent's __init__ method
        self.menu = menu

    def describe_menu(self):
        """describe menus"""
        print(f"{self.name} is a {self.type} restaunrant, serving {self.menu}")

new_rest1 = Restaurant('McDonald','fastfood')
new_rest1.describe_rest()
new_rest1.open_rest()

new_rest2 = Restaurant('BBQ','fried chicken')
new_rest2.describe_rest()
new_rest2.open_rest()

new_rest3 = Foodstand('Subway','sandwich','vegie toasts')
new_rest3.describe_menu()

# call a class from another py file
alice_toy = Toy('woody','yellow',20)
alice_toy.color_print()

#import random module
print(randint(1,6))
colors = ['red','yellow','orange']
recommendation = choice(colors)
print(recommendation)
