import matplotlib.pyplot as plt
import random

data = []
for i in range(50):
    data.append(random.randint(0,100))
# print(data)

data2 = [random.randint(0,100) for _ in range(50)]
# print(data2)
fig, ax = plt.subplots()
ax.hist(data2)
ax.set_xlabel('n')
ax.set_ylabel('number of n')
ax.set_title('randum numbers')
plt.savefig("myhistogram.png")
plt.show()