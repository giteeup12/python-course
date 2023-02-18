import random
def new_func():
    roll = random.randint(1,6)
    return roll

roll = new_func()
print("hello")
userguess = int(input("guess the number on the dice\n"))
if userguess == roll:
    print("your guess was correct")
username = 'sa'
print(username + '\n')
