class Toy:
    def __init__(self, name, color, age) :
        self.name = name
        self.color = color
        self.age = age
    
    def color_print(self):
        """toy's color"""
        print(f"{self.name} is {self.color}")

# separate some methods from the parent : "composition"
class Toy_size:
    def __init__(self, width=20, height=3) :
        self.width = width
        self.height = height
        self.unit1 = 'cm'
        self.unit2 = 'inch'

    def print_size(self):
        print(f"its width is {self.width} {self.unit1} and height {self.height}{self.unit2}")

class Wooden_toy(Toy): # Wooden_toy extends Toy
    def __init__(self, name, color, age) :
        """bring parent's attributes"""
        super().__init__(name, color, age) # call parent's __init__ method
        self.size = Toy_size() # use an instance of the class Toy_size as child's attribute

    def color_print(self): # override parent's method
        """override parent's method color_print"""
        print(f"{self.color} is your toy!")

catherin_toy = Wooden_toy('alan','green',30000)
catherin_toy.color_print()
print(catherin_toy.size.width, catherin_toy.size.unit1) # use Toy_size's attributes
catherin_toy.size.print_size() # use Toy_size's method
