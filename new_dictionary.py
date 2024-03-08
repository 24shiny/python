acc_color = {'hat':'green', 'pants':'blue', 'T-shirt':'yellow'}
print(acc_color)
acc_color_reverse = {v:k for k,v in acc_color.items()}
print(acc_color_reverse)

std1 = {'name':'J','grade':'A'}
std2 = {'name':'Y', 'grade':'B'}
std3 = {'name':'S', 'grade':'C'}
stdInfo = [std1, std2, std3]

print(stdInfo[0].get('name'))

# if std4 in stdInfo:
#     stdInfo[3]

for row in std1.items():
    print(row, type(row))

for r,v in std1.items():
    print(r,v, type(r),type(v))

a = [4,1,6,9,3]
a_copy = sorted(a)
print(a,a_copy)

stdDb = {'J':85, 'A':90, 'C':72}

first = lambda x:x[0]
second = lambda x:x[1]

first = lambda x:x[0]
print(first(row), second(row))

# sort by value
print(sorted(stdDb.items(), key=second, reverse=True))

# check whether number cards of two match
# lst = input().split()
# comp_lst = input().split()
# match = 0
# for i in comp_lst:
#     if(i in lst): match +=1
# print(match)

db = {} # dictionary
db['a'] = list()
db['a'].append('1')
db['a'].append('J')
db['a'].append('B')
print(db)

def add(x,y):
    return x+y

print(add('a','b'))
print(add(1,2))

a = [i for i in range(5)]
print(a)
b = []
# while (False in a):
#     popped = a.pop()
#     b.append(popped)
# print(a,b)

while a:
    popped = a.pop()
    b.append(popped)
print(a,b)

#remove a certain element
alphabet = ['a','b','c','d','b','a','b']
alphabet.remove('b')
print(alphabet)

#remove all the certain elements -> use while
while 'b' in alphabet:
    alphabet.remove('b')
print(alphabet)




