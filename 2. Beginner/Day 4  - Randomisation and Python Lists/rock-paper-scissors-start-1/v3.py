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

row1 = [0, 1, 2]
row2 = [2, 0, 1]
row3 = [1, 2, 0]
map = [row1, row2, row3]

your_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if your_choice < 0 or your_choice > 2:
    print("Don\'t enter numbers out of scope!'")
    exit()

print(map[your_choice])

comp_choice = random.randint(0, 2)
print(f"Computer chose:\n{map[comp_choice]}")

# human won for flag 1, pc for 2 , draw for 0
result = map[comp_choice][your_choice]
if result == 0:
    print("It is a draw")
elif result == 1:
    print("You won!")
elif result == 2:
    print("You lose")
