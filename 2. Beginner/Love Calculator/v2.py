##### Much more complex code which is not much efficient #####

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


def love_calculator(name, word):
    total = 0
    for letter in word.lower():
        total += name.lower().count(letter)
    return total


def get_number(name1, name2, word):
    return love_calculator(name1, word) + love_calculator(name2, word)


first_word = 'true'
second_word = 'love'

first_number = get_number(name1, name2, first_word)
second_number = get_number(name1, name2, second_word)

score = int(f'{first_number}{second_number}')
message = f'Your score is {score}'

if score < 10 or score > 90:
    message += ', you go together like coke and mentos.'
elif 40 <= score <= 50:
    message += ', you are alright together.'
else:
    message += '.'

print(message)
