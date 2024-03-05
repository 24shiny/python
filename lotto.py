from random import randint
from random import choices
from random import choice
import random
import string

lotto_array = []
for i in range(10):
    lotto_array.append(randint(1,46))
print(lotto_array)


# for i in range(5):
#     lotto_array.append(choices(string.ascii_letters))
# print(lotto_array)

# winners = []
# for i in range(4):
#     winners.append(choice(lotto_array))
# print(winners)

# print(f"winning numbers are {winners}")

# my_ticket = []

ll = list(range(10))

print(random.sample(ll, 2))
# [6, 9, 0, 2, 4, 3, 5, 1, 8, 7]