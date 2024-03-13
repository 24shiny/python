import matplotlib.pyplot as plt
import random
from random import choice

data1 = [random.randint(0,200) for _ in range(500)]
data2 = [random.randint(0,200) for _ in range(500)]
# print(data2)
fig, ax = plt.subplots()
ax.plot(data1[:100],data2[:100], color='red')
ax.scatter(data1[:100],data2[:100], color='red')
ax.plot(data1[100:],data2[100:], color='blue')
ax.scatter(data1[100:],data2[100:], color='blue')
ax.set_title('random values')
plt.show()

# initialize settings
x= 0
y=0
x_data = []
y_data = []
x_data.append(x)
y_data.append(y)
x_mov = [-5,5]
y_mov = [-5,5]
for i in range(100):
    x = x + choice(x_mov)
    x_data.append(x)
    y = y + choice(y_mov)
    y_data.append(y)

fig, ax = plt.subplots()
ax.scatter(x_data,y_data)
ax.plot(x_data,y_data)
plt.show()