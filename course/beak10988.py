# check whether a given word is palindrome or not
a = 'level'
b = 'beakjoon'
c = 'noon'

def checkpalindrome(word):
    i = 0
    bool_arr = []
    while(i<len(word)/2):
        # print(word[i]==word[len(word)-1-i])
        bool_arr.append(word[i]==word[len(word)-1-i])
        i += 1

    if False in bool_arr:
        return False
    else:
        return True
    
print(checkpalindrome(a))
print(checkpalindrome(b))
print(checkpalindrome(c))
