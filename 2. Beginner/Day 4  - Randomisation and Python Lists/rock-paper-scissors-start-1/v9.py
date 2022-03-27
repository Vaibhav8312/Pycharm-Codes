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

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

choice = [rock, paper, scissors]


computer_choice = random.randint(0, 2)

#                    Used rock   Used paper  Used scissors
computer_rock =     ["You draw", "You win",  "You lose"]
computer_paper =    ["You lose", "You draw", "You win"]
computer_scissors = ["You win",  "You lose", "You draw"]

horizontal = [computer_rock, computer_paper, computer_scissors]

result = horizontal[computer_choice][user_choice]

# prints what you used
print(choice[user_choice])
# prints what the computer used
print("Computer chose:\n" + choice[computer_choice])
# prints outcome
print(result)
