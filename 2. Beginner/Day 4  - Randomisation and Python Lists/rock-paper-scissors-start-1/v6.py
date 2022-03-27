import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
choices = [rock, paper, scissors]
player_choice = int(input("What do you want to choose? Enter 0 for Rock, 1 for Paper and 2 for Scissors.\n"))

computer_choice = random.randint(0, 2)

print(choices[player_choice])
print(choices[computer_choice])

if player_choice > 2:
    print("You cheat")

# this describes all situations when computer is winning
elif computer_choice == player_choice + 1 or computer_choice + 2 == player_choice:
    print("You win")

# this describes the equals
elif computer_choice == player_choice:
    print("It's a draw")

# the rest is me winning
else:
    print("I win")