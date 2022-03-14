c,s=map(int,input().split())
co=[int(x) for x in input().split()]
cod=dict(
    ("C-{}".format(i+1),
    float(co[i]))
    for i in range(len(co))
)
score=[]
data=[]
for i in range(s):
  sd=[x for x in input().split(",")]
  data.append((sd[0],sd[2],sd[3],sd[4]))
  score.append(float(sd[1]))

print(co)
print(cod)
print(score)
print(data)

for i in range(s):
  if(cod[data[score.index(max(score))][1]]>0):
    cod[data[score.index(max(score))][1]]-=1
    print(data[score.index(max(score))][0],data[score.index(max(score))][1])
    score[score.index(max(score))]=0
  elif(cod[data[score.index(max(score))][2]]>0):
    cod[data[score.index(max(score))][2]]-=1
    print(data[score.index(max(score))][0],data[score.index(max(score))][2])
    score[score.index(max(score))]=0
  elif(cod[data[score.index(max(score))][3]]>0):
    cod[data[score.index(max(score))][3]]-=1
    print(data[score.index(max(score))][0],data[score.index(max(score))][3])
    score[score.index(max(score))]=0