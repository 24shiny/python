# data = []
# for _ in range(2):
#     get_input = int(input("enter an input : "))
#     data.append(get_input%42)
# data2 = [int(input()) % 42 for _ in range(3)]
#set(data)

#get ten inputs and calculate their remainder when divided by 42
data = [int(input())%42 for _ in range(10)]
# remove overlapped values by "set" set(data)
print(data)
result = set(data)
print(result)
