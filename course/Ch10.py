# ways to import an external file
#1
from pathlib import Path
path = Path('greeting.txt')
print(path)
contents = path.read_text()
print(contents)
#2
with open('greeting.txt') as file:
    for line in file:
        # print(line, end='')
        print(line.rstrip())

# set defualt values when defining a function
def add(a=1,b=2):
    return a+b

print(add())
print(add(3,4))

#import a csv file
import csv
with open('grades.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)
    # header = next(reader)
    # for hrow in header:
    #     print(hrow)
        
import os
for item in os.listdir():
    # print(item) print all files in the directory
    if '.txt' in item:
        print(item) # print only txt files

file_path = Path('grades.csv')
print(os.path.exists(file_path))
print(file_path.exists())
file_path_list = str(file_path).split(".")
print(file_path_list)

import json
numbers = [2,9,5,4,3,6]
items = json.dumps(numbers) # list to json array
path = Path('numbers.json')
path.write_text(items)

# load json file
items_copy = path.read_text()
numbers_copy = json.loads(items_copy)
print(numbers_copy)

# another example of json
data = '{"name":"kim", "age":40, "gender":"male"}'
data2 = {"name":"Lee", "age":12, "gender":"female"}
with open('member.json','w'):
    items = json.dumps(data)
path = Path('member.json')
path.write_text(items)

items2 = json.dumps(data2) 
print(items2, type(items2))
# str type data from server to its client
items2_1 = json.loads(items2)
print(items2_1, type(items2_1),items2_1["age"])
# dic type data from the client to its server

import pickle
new_data = [1,5,3,4,6]
with open('new_member.pk','rb') as w_file:
    pickle.dump(data,'new_member.pk')
new_data2 = pickle.load('new_member.pk')
