#3-1,2
my_frirends = ["Alice","Bob","Cathy"]
for i in my_frirends:
    print("morning,",i)

#3-3 wishlist
colors = ['red','green','blue']
cloth = ['T-shirt','jacket']
print("\nhere is my wishlist:")
for i in colors:
    for j in cloth:
        print("I would love to get a", i, j)

#3-4 dinner invitation
print("\nlet me send inviation messages to my friends:")
for i in my_frirends:
    print(i,", would you like to come to dinner today?")

#3-5 change the list
print("\nOh,",my_frirends[1],"says he cannot come")
my_frirends[1] = "David"
print("\nlet me resend inviation messages to my friends:")
for i in my_frirends:
    print(i,", would you like to come to dinner today?")

popped_friend = my_frirends.pop(0)
print("\nOh,",popped_friend,"says she cannot come")
print("Eric will come instead")
my_frirends.insert(0,"Eric")
for i in my_frirends:
    print(i,", would you like to come to dinner today?")

#3-6 more guests
my_frirends.append("Fredric")
my_frirends.insert(2,"Henry")
print("\nnew list: ",my_frirends)

#3-7 delay in delivery
for i in range(1,4):
    popped_friend_delayed = my_frirends.pop()
    print("sorry",popped_friend_delayed,", see you next time")
print(my_frirends)

