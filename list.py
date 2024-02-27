import random as rd

# create a list and .append & .insert(index,obj)
color = ['red','orange']
color.append('green')
color.insert(1,'yellow')
print(color)

# delete an element by del, remove
color.append('purple')
print(color)
del color[4]
print(color)

color.append('purple')
print(color)
color.remove('purple')
print(color)

# if you'd like to use one out of the list, use pop(index).
color.append('purple')
popped_color1 = color.pop() 
print(popped_color1)
print(color) 

# select what to pop by inserting its index
popped_color2 = color.pop(0)
print(popped_color2)
print(color)

# list and for-loop
sqauares = [i**2 for i in range(1,11)]
print(sqauares)

# two ways to generate an odd list
odd1 = list(range(1,20,2))
print(odd1)

odd2 = [2*i-1 for i in range(1,11)]
print(odd2)

three_multiples = [3*i for i in range(1,11)]
print(three_multiples)

triples = [i**3 for i in range(1,11)]
print(triples)

#copy list
my_frirends = ["Alice","Bob","Cathy"]
my_frirends_copy = my_frirends[:]
print(my_frirends)
print(my_frirends_copy)

# 1d array filled with randum numbers
rd_array=[]
for i in range(10):
    rd_array.append(rd.randint(1,10))
print(rd_array)
rd_array.sort()
print(rd_array)

# 2d array filled with randum numbers
rd_array2=[]
for i in range(2):
    temp = []
    rd_array2.append(temp)
    for j in range(3):
        temp.append(round(rd.random(),3))
print(rd_array2)

# concatenate lists
a = [1,2]
b = [3,4]
print(a+b)
print(a*3)

