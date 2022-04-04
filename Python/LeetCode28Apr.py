def fun():
    return False

mat = [
    [1,1,0,0,0],
    [1,1,1,1,0],
    [1,0,0,0,0],
    [1,1,0,0,0],
     [1,1,1,1,1]]
k = 3
rowsPower = []
index = 0
for i in mat:
    count = 0
    for j in i:
        if j == 1:
            count+=1
    rowsPower.append([count,index])
    index+=1
rowsPower.sort()
newArr = []
for i in range(0,k):
    newArr.append(rowsPower[i][1])

print(newArr)