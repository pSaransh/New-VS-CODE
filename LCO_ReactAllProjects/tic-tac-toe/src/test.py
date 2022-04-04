def getNumber(array):
    num = 0
    #array = array[::-1]
    for i in array:
        num += i
        num *= 10
    return num//10

res = str(getNumber([4,3,2,2]))
l = list(res)
print(l)
returningArr = list(map(int, l))
print(returningArr)