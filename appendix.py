def get_data():
    return 1,2,3

class Shape:
    def __init__(self,base,height) -> None:
        self.__base = base
        self.height = height
    
    @property #getter, read only
    def get_base(self):
        return self.__base
    
    @height.setter
    def height(self):
        return self.height
    
_,b,c = get_data() # not to get the first element, use underline(_)
print(b,c)

a=[1,2,3]
b=[11,22,33]
mylist = [*a,*b] # *array refer to all elements in the array
print(mylist)

c = ['a','b']
z = zip(a,c) # zip gives you pairs of a and c arrays
print(list(z))

###getters and setters
@