def canBeInserted(alreadyPresent,toBeInserted):
    alreadyPresentSize = alreadyPresent[2]
    toBeInsertedSize = toBeInserted[1]
    if len(alreadyPresentSize)==2 and len(toBeInsertedSize)==2: 
            return alreadyPresentSize>=toBeInsertedSize
    if len(alreadyPresentSize) == len(toBeInsertedSize): 
            if(alreadyPresentSize[1]==toBeInsertedSize[1]):
                return alreadyPresentSize>=toBeInsertedSize
            elif(alreadyPresentSize[1]=='k' and toBeInsertedSize[1]=='m'):
                return False
            else: return True
    return False
present = int(input())
j=0
file_in_doc = []
while j<present:
    file = input().split()
    file_in_doc.append(file)
    j+=1

to_be = int(input())
j=0
file_to_be = []
while j<to_be:
    file = input().split()
    file_to_be.append(file)
    j+=1

output_files = []
j=0
#in between
for i in file_in_doc:
    ind = file_in_doc.index(i)
    if i[-1]=='1':
        if(canBeInserted(i,file_to_be[j])):
            output_files.append([file_to_be[j][0],i[1]])
            file_to_be.pop(0)


#at last
offset = 
for i in file_to_be:
    offset = 
    output_files.append([i[0],])