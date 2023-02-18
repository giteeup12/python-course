import random
dice = random.randint(1,6)
print('dice show: ' + str(dice))
dice_was1 = 0
dice_was2 = 0
dice_was3 = 0
dice_was4 = 0
dice_was5 = 0
dice_was6 = 0

for x in range(1,100000):
    dice = random.randint(1,6)
    print('dice was: ' + str(dice))
    if dice == 6:
        dice_was6 = dice_was6 + 1
    elif dice == 5:
        dice_was5 = dice_was5 + 1
    elif dice == 4:
        dice_was4 = dice_was4 + 1
    elif dice == 3:
        dice_was3 = dice_was3 + 1
    elif dice == 2:
        dice_was2 = dice_was2 + 1
    else:
        dice_was1 = dice_was1 + 1
print ('it was 1:' + str(dice_was1) + ' times')
print ('it was 2:' + str(dice_was2) + ' times')
print ('it was 3:' + str(dice_was3) + ' times')
print ('it was 4:' + str(dice_was4) + ' times')
print ('it was 5:' + str(dice_was5) + ' times')
print ('it was 6:' + str(dice_was6) + ' times')

