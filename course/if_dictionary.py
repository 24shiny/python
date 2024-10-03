# if
cars = ['audi','bmw','subaru','toyota']
for i in cars:
    if(i=='bmw'):
        print(i.upper())
    else:
        print(i.title())

print('honda' in cars)

#dictionary
alien1 = {'name':'Alan','color':'green','age':'1000'}
#find a value corresponding to a key
print(alien1['name'])
print(alien1['color'])
#find a value corresponding to a key with get()
print(alien1.get('name'))
print(alien1.get('lrod','unkown'))
#add a pair of elements
alien1['planet']='mars'
print(alien1)
#change a value with key, when the key already exists
alien1['color']='yellow'
print(alien1)
#delete a key-value pair with key
alien1['lord']='woody'
print(alien1)
del alien1['lord']
print(alien1)

#transverse the dictionary
fruit = {'Banana':'yellow','Orange':'orange','Apple':'red','tangerin':'orange'}
for name in fruit.keys():
    print(name)
for color in fruit.values():
    print(color)
# sorted method can be applied to both keys and values
for name, color in sorted(fruit.items()):
    print(f"{name} is {color}")

# when there are more than two keys having the same value
fruit_added = {'Banana':'yellow','Orange':'orange','Apple':'red','tangerin':'orange'}
for color in set(fruit_added.values()):
    print(color)

# nesting : dictionaries in a list
toy1 = {'name':'woody','color':'yellow','age':'30'}
toy2 = {'name':'buzz','color':'violet','age':'200'}
toy3 = {'name':'Alan','color':'green','age':'1000'} 
toys = [toy1, toy2, toy3]
print(toys)

# nesting : lists in a dictionary
pizza = {'crust':'thin','toppings':['mushrooms','onions']}
for ingredients in pizza['toppings']:
    print(ingredients)

# nesting : dictionaries in a dictionary
toys_dic = {
        'toy1' : {'name':'woody','color':'yellow','age':'30'},
        'toy2' : {'name':'buzz','color':'violet','age':'200'}
    }
for num, info in toys_dic.items():
    description1 = f"{num}\'s name is {info['name']}"
    description2 = f"It is {info['color']} and {info['age']} years old"
    print(description1)
    print(description2)
