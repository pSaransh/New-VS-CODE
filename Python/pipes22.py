from pipe import *
arr = [1,2,3,4,5]

#where
wh = list(arr | where(lambda x:x%2==0))
print(wh)

#select
sl = list(arr | select(lambda x:x*2))
print(sl)

#select,where
slwh = list(arr
            | where(lambda key:key%2!=0)
            | select(lambda key:key**2))
print(slwh)

#chain nested -> unnested but only outer arr
nested = [[1,2,[3]],[4,5]]
ch = list(nested|chain)
print(ch)

#traverse nested -> n-D to 1-D where n⋸N
tr = list(nested|traverse)
print(tr)

#groupby
print(
    list(
        (1,2,3,4,5,6,7,8,9,0)
        | groupby(lambda x:'Even' if x%2==0 else 'Odd') #[('Even', <itertools._grouper at 0x7fbea8030550>),
                                                        #('Odd', <itertools._grouper at 0x7fbea80309a0>)]
        | select(lambda x: {x[0]:list(x[1])})           #[{'Even': [2, 4, 6, 8]}, {'Odd': [1, 3, 5, 7, 9]}]
    )
)
#can use where in this too

#dedup -> deduplicate values using func or w/o it.
arr = (1,2,1,2,2,1,3,4,6,2,3,4,7,8,9,3,5,6,7,8,9,6,4,6,5,7,0,1,2,8)
print(list(arr|dedup))
print(list(arr|dedup(lambda x:x<7)))

data = [
    {"name":'apple','price':10,'count':2},
    {"name":'orange','price':7,'count':None},
    {"name":'pineapple','price':24,'count':8},
]
print(
    list(
        data
        | dedup(key=lambda fruit:fruit['name'])
        | select(lambda fruit:fruit['count'])
        | where(lambda count: isinstance(count,int))
    )
)