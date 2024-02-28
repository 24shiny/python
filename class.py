class Moving_toy:
    def __init__(self, name, color, age) :
        self.name = name
        self.color = color
        self.age = age
    
    def color_print(self):
        """toy's color"""
        your_color = f"{self.name} is {self.color}"
        return your_color

    def age_print(self):
        """toy's age"""
        print(f"{self.name} is {self.age} years old")

# create instances of the class Moving_toy
alice_toy = Moving_toy('woody','yellow',20)
bob_toy = Moving_toy('buzz','violet',1000)

# use methods of the class
print(alice_toy.color_print())
bob_toy.age_print()
