import random
roll = random.randint(1,6)
print("hello")
userguess = int(input("guess the number on the dice\n"))
if userguess == roll:
    print("your guess was correct")
