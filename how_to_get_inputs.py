#1
n = int(input())
# for example, enter 3
print(n)

#2 
# for example, enter 2 3
a, b = map(int, input().split())
print(a, b)

#3
# for example, enter 10 40 30 60 50
numbers = list(map(int, input().split()))
print(numbers)


# 4
import sys
# press ctr+z to end entering an input
data1 = sys.stdin.readlines() #EOF
print(data1)
data2 = [int(d.rstrip()) for d in sys.stdin.readlines()]
print(data2)

# print("/n".join(data2))