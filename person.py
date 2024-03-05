class Person:
    objCount = 0 # class's variables
    def __init__(self, name, age, address) -> None:
        self.name = name # instance's variables
        self.age = age
        self.address = address
        self.weight = 50 #public
        self.tall = 1.55
        self.weightChange = [45,51,48,55,43]
        self.__vision = 1.0 #private -- accessed by a method
        Person.objCount +=1 # increase by one every time a new object is created
        print("object {} is created".format(self.name))

    @classmethod # a decorator is to python and an annotation is to java
    def printing(cls): # class method
        print(cls.objCount)

    def show_vision(self):
        print(f"{self.name}'s vision is {self.__vision}")

    def __str__(self):
        return "{}\t{}\t{}\t".format(self.name,self.age,self.address)
    
    def __len__(self):
        return len(self.weightChange)
    
    def __eq__(self,another):
        return self.address == another.address
    
    def __call__(self):
        # return self.weight/(self.tall**2)
        print(f"I am {self.name} living in {self.address}")

    def __getitem__(self,index):
        return self.weightChange[index]

    def __del__(self):
        print("object {} is deleted".format(self.name))

# without a reference, this object is deleted right after being created
Person('Park', 10, 'Jeju')

new_person = Person('Kim', 23, 'Busan')
another_person = Person('Lee', 56, 'Busan')
new_person.show_vision()

# print(str(new_person))
print(new_person.__str__())
print(str(new_person))
print(new_person) # print method automatically call the str method

print(len(new_person))
print(new_person == another_person) # __eq__ method

# instances behave like functions
# 
new_person()
print(new_person[2])

print(type(new_person))
print(type(new_person[2]))
print(isinstance(new_person,Person))
# print(isinstance(Person,new_person)) watch out their order! isinstance(instance,class)

print(f"{new_person.name}'s age is ***{new_person.age:4}***")
#all give the same result as all the Person't objects share the field
print("# of created objects is ", Person.objCount)
print("# of created objects is ", new_person.objCount)
print("# of created objects is ", another_person.objCount) 

Person.printing() # class method
new_person.printing() # get the same result