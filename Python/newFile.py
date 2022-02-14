from itertools import *
s1 = "ab"
s2 = "dbao"
lst = list(permutations(s1))
lst2 = list(permutations(s2,2))
print(lst)
print(lst2)
for i in lst:
    if i in lst2:
        print('True')
else:
    print('False')
