class Toy:
    def __init__(self, name, color, age) :
        self.name = name
        self.color = color
        self.age = age
    
    def color_print(self):
        """toy's color"""
        print(f"{self.name} is {self.color}")
    
class Wooden_toy(Toy): # Wooden_toy extends Toy
    def __init__(self, name, color, age) :
        """bring parent's attributes"""
        super().__init__(name, color, age) # call parent's __init__ method
        self.size = 5

    def print_size(self):
        print(self.size)

    def color_print(self): # override parent's method
        """override parent's method color_print"""
        print(f"{self.color} is your toy!")

alice_toy = Toy('woody','yellow',20)
alice_toy.color_print()

bob_toy = Wooden_toy('buzz','violet',1000)
bob_toy.color_print() # compare results and check method-override
bob_toy.print_size() 