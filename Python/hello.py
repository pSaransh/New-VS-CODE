def isValid(n,k):
    nCopy=n
    while n>0:
        rem = n%10
        if(rem!=4 and rem!=5 and rem!=6):
            return False
        n=n//10
    if(nCopy%k==0):
        return True
    else:
        return False
def getNums(n,k):
    l=[]
    for i in range(1,n+1):
        if isValid(i,k):
            l.append(i)
    return l
n=100
k=2
items=getNums(n,k)
for i in items:
    print(i,end=" ")
    