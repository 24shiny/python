# average and median
numbers = list(map(int, input().split()))
# inputs = 10 40 30 60 50
# print their average

def findAve(list):
    return sum(numbers)/len(list)

def findMed(list):
    numbers.sort()
    return numbers[int(len(list)/2)]

print(findAve(numbers))
print(findMed(numbers))

