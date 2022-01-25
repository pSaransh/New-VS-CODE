import random as r
print('-----Welcome to the game-----')
name = input('Enter player name: ')
print('🎮🎮🎮 Welcome {} 🎮🎮🎮'.format(name))
print('Legends:')
print('R: 🪨')
print('P: 📃')
print('S: ✂️')
print('Press E to finish the game...')
user_score,computer_score=0,0
while True:
    print('Enter your choice:  🪨  📃 ✂️')
    user_choice = input().capitalize()
    if user_choice=='E':
        if input('Do you want to check scores?(Y/N) ').capitalize()=='Y':
            print('Computer:',computer_score)
            print('{}:{}'.format(name,user_score))
        print('Ciao 👋')
        exit(0)
    else:
        random_choice = r.randint(1,3)
        if random_choice==1 and user_choice=='S':
            computer_score+=1
            print('Computer Won.🪨')
            print('Try Again...')
        if random_choice==2 and user_choice=='R':
            computer_score+=1
            print('Computer Won.📃')
            print('Try Again...')
        if random_choice==3 and user_choice=='P':
            computer_score+=1
            print('Computer Won.✂️')
            print('Try Again...')
        if random_choice==1 and user_choice=='P':
            user_score+=1
            print('You Won.🪨')
            print('Play Again...')
        if random_choice==2 and user_choice=='S':
            user_score+=1
            print('You Won.📃')
            print('Play Again...')
        if random_choice==3 and user_choice=='R':
            user_score+=1
            print('You Won.✂️')
            print('Play Again...')
        if random_choice==user_choice:
            print('Tie')
            print('Try Again')
        else: print('Enter right choice.')