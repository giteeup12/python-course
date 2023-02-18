import random
computer_choice = random.choice(['rock', 'paper', 'scissors'])
user_choice = input("enter 'rock', 'paper', or 'scissors' ")
if computer_choice == user_choice:
    print('tie')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print ('win, the computer had ' + computer_choice)
elif user_choice == 'paper' and computer_choice == 'rock':
    print ('Win, the computer had ' + computer_choice)
elif user_choice == 'scissors' and computer_choice == 'paper':
    print ('win, the computer had: ' + computer_choice)
else:
    print ('you lose: the computer had: ' + computer_choice)