import random
roll = random.randint(1,6)
guess = int(input("enter your guess\n"))
if roll == guess:
    print('you were right')
else:
    print('you were wrong: the answer was ' + str(roll) + '\n')
