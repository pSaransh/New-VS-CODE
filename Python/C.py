def isColinear(three_points_list):
    x1 = three_points_list[0][0]
    x2 = three_points_list[1][0]
    x3 = three_points_list[2][0]
    y1 = three_points_list[0][1]
    y2 = three_points_list[1][1]
    y3 = three_points_list[2][1]
    disc = x1*(y2-y3) - x2*(y1-y3) + x3*(y1-y2)
    if(disc == 0): return True
    return False

from itertools import combinations as c
n = int(input())
i=0
points = []
while i<n:
    point = list(map(int,input().split()))
    points.append(point)
    i+=1

side_count=0
l = list(c(points,3))
for i in l:
    if(isColinear(i)):side_count+=1

print(n-side_count)