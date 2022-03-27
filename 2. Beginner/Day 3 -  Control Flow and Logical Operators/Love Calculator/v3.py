# Much shortened code

name_1 = (input("Partner 1: ") + input("Partner 2: ")).lower()
true = name_1.count('t') + name_1.count('r') + name_1.count('u') + name_1.count('e')
love = name_1.count('l') + name_1.count('o') + name_1.count('v') + name_1.count('v')
score = int(str(true) + str(love))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}.")