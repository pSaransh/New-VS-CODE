list1=["mark","eminem","john","logan"]
def frn(x):
    i=0
    list3 = []
    while(i<=3):
        if len(x[i])<5:
            app=x.pop(i)
            list3.append(app)
        i+=1
    return list3
result = frn(list1)
print(result)