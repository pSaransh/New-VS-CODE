def getSumOfRange(n,m):
    sum=0
    for i in range(n,m+1):
        sum+=i
    return sum

n = int(input('Enter the first integer: '))
m = int(input('Enter the second integer: '))
print(getSumOfRange(n,m))
