# #input
# number_of_commands = int(input())
# commands = []
# i=0
# while i<number_of_commands:
#     sub_command = input()
#     list_sub_commands = sub_command.split()
#     commands.append(list_sub_commands)
#     i+=1
# print('Output')
# for i in commands:
#     print(*i)
c = []
n = int(input())
for i in range(0,n):
    a = input()
    b = a.split()
    if(b[0]=='insert'):
        c.insert(int(b[1]),int(b[2]))
        print(c)
