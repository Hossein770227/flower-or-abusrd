import os 
import random 
os.system('cls')

input_cups =int(input('How many cups ? '))
input_chances=int(input('How many chances ? '))

def check_gessing():
    ai_goal=random.randint(1,input_cups)
    for i in range(input_chances):
        print('-'*30)
        print(f'{input_chances-i} chances left!')
        user_choices=int(input('Enter you Gess: '))
        if user_choices==ai_goal:
            print('-'*30)
            print('You won!')
            return
        else:
            print('you gess is wrong.')
            print('Please try again.')

    print('-'*30)         
    print('Sorry.You Lost!')

check_gessing()
