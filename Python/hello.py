n = int(input())
nC = n
ls = []
while n>0:
    scores = list(map(int,input().split()))
    ls.append(scores)
    n-=1
print(ls)
for i in ls:
    diff = i[1]-i[0]
    if diff>=0:
        i.append(abs(diff))
        i.append(2)
    else:
        i.append(abs(diff))
        i.append(1)
leads = []
for i in ls:
    tp = [i[2],i[3]]
    leads.append(tp)
    
print(ls)
print(leads)
max = leads[0][0]
for i in leads:
    if max<=i[0]:
        max=i[0]
print(max)
player = 0
for i in leads:
    if max==i[0]:
        player = i[1]

print(player,max)