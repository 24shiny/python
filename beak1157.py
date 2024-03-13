from collections import Counter
import string

# find the most used alphabet
a = 'MiSsisSIpi'
b = 'BAnaNa'

def most_used_alphabet(word):
    al_list = Counter(word.lower()).most_common()
    if(al_list[0][1]==al_list[1][1]):
        return '?'
    else:
        return al_list[0][0]

print(most_used_alphabet(a))
print(most_used_alphabet(b))

# from collections import Counter
# print(Counter(a.lower()))
# print(Counter(a.lower()).most_common())
# al_list = Counter(a.lower()).most_common()
# print(al_list)
# print(al_list[0][1])
# print(al_list[1][1])

def most_used_alphabet2(word):
    word_l = word.lower()
    C = {l:word_l.count(l) for l in string.digits + string.ascii_lowercase}
    sortedC = sorted(C.items(), key=lambda x:x[1], reverse=True)
    if(sortedC[0][1]==sortedC[1][1]):
        return '?'
    else:
        return sortedC[0][0]

print(most_used_alphabet2(a))
print(most_used_alphabet2(b))

# print(string.digits)
# print(string.ascii_lowercase)
# s = a.lower()
# C = {l:s.count(l) for l in string.digits + string.ascii_lowercase}
# r = sorted(C.items(), key=lambda x:x[1], reverse=True)
# print(r)



