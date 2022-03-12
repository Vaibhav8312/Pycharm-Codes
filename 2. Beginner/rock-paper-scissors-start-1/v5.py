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

outcome = ["It is a draw!", "You win!", "You lose!"]
print(outcome[player_choice - computer_choice])
