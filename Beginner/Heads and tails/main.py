import random

print('Toss A Coin To Your Witcher!')
choice = 'y'
while choice == 'y':
    coin = random.randint(0, 1)
    if coin:
        print('Ekimmara Heads')
    else:
        print('Forktails')
    choice = input('Do you want to continue? (y/n) ')
print('Bye!')

# # In Python 3.x True and False are keywords and will always be equal to 1 and 0.
# 0 == False
# 1 == True
