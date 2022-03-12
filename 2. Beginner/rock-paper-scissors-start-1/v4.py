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

prints = {
    -1: "You lost",
    0: "You draw",
    1: "You win"
}

results_map = [
    # rock, paper, scissors
    (0, -1, 1),  # rock
    (1, 0, -1),  # paper
    (-1, 1, 0),  # scissors
]

choices = [rock, paper, scissors]

player_choice = int(input("What do u choose? 0 for rock, 1 for paper, 2 for scissors > "))
print("Your choice:\n", choices[player_choice])

computer_choice = random.choice(choices)
print("Computer choice:\n", computer_choice)

result = results_map[player_choice][choices.index(computer_choice)]

print(prints[result])
