def getBitwiseAND(acc):
    res = 0
    for i in acc:
        res &= i
    return res

def sub_lists (l):
    lists = [[]]
    for i in range(len(l) + 1):
        for j in range(i):
            lists.append(l[j: i])
    return lists
#from itertools import *
# Read the variable from STDIN
tc = int(input())
while tc > 0:
    n = int(input())
    sum = 0
    arr = list(map(int, input().split()))
    subsets = sub_lists(arr)
    for i in subsets:
        res = getBitwiseAND(i)
        sum += res
    print(sum)
    tc-=1
