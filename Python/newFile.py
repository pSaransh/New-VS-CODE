def deleteOcc(string):
    i=0
    while i<len(string):
        if string[i:i+2] in string[i+2:]: print(string[i:1+2])
        i+=2            
# n = input()
deleteOcc('1432451465142014')