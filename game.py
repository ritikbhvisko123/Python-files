import random 
# opt = ['rock','paper','scissors']

# computer_choice = random.choice(opt)

print('Rock Paper scissors Game')
print({0:'Rock',1:'Paper',2:'Scissors'})
# print('You have only 10 chances')



# c_choice = random.choice(opt)
# y_choice = int(input('Enter your choice '))

# y_value=''

# if y_choice==0:
#     y_value='rock'
# elif y_choice==1:
#     y_value='paper'
# elif y_choice==2:
#     y_value='scissors'

print("Let's Play the Game Enter 1 to start and 0 to exit ")
num = int(input( ))

if num==1:
    i = 1
    your_count = 0
    computer_count = 0

    while i<10:
        opt = ['rock','paper','scissors']
        c_choice = random.choice(opt)
        y_choice = int(input('Enter your choice '))

        y_value = ''
        if y_choice ==0:
            y_value='rock'
        elif y_choice==1:
            y_value='paper'
        elif y_choice==2:
            y_value='scissors'
        else:
            print('Please Enter correct number ')
            break


        if y_value==c_choice:
            print('Game Tie \n')
            print(f'your choice {y_value} and computer choice {c_choice}')
            your_count = your_count+ 1
            computer_count = computer_count+1
            print(10-i,'choices left')


        elif y_value=='paper' and c_choice=='rock':
            print('You won! \n ')
            print(f'your choice {y_value} and computer choice {c_choice}')
            your_count = your_count+ 1
            print(10-i,'choices left')


        elif y_value=='paper' and c_choice=='scissors':
            print('Computer won! \n')
            print(f'your choice {y_value} and computer choice {c_choice}')
            computer_count = computer_count+1
            print(10-i,'choices left')


        elif y_value=='scissors' and c_choice=='rock':
            print('Computer won! \n')
            print(f'your choice {y_value} and computer choice {c_choice}')
            computer_count = computer_count+1
            print(10-i,'choices left')

        elif y_value=='scissors' and c_choice=='paper':
            print('You won! \n')
            print(f'your choice {y_value} and computer choice {c_choice}')
            your_count = your_count+ 1
            print(10-i,'choices left')


        elif y_value=='rock' and c_choice=='paper':
            print('Computer won! \n ')
            print(f'your choice {y_value} and computer choice {c_choice}')
            computer_count = computer_count+1
            print(10-i,'choices left')

        elif y_value=='rock' and c_choice=='scissors':
            print('You won! \n ')
            print(f'your choice {y_value} and computer choice {c_choice}')
            your_count = your_count+1
            print(10-i,'choices left')
        i = i+1



    if your_count>computer_count:
        print('You Are the Winner',your_count,'your_count',computer_count,'computer_count')
    else:
        print('You lost the Game',your_count,'your_count',computer_count,'computer_count')

else:
    print('Exits')




    
        


