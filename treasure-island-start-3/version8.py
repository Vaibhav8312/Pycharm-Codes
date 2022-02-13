print(
    """ 
      ____                     
     /  __\          ____                     
     \( oo          (___ \                     
     _\_o/           oo~)/
    / \|/ \         _\-_/_
   / / __\ \___    / \|/  
   \ \|   |__/_)  / / .- \ 
    \/_)  |       \ \ .  /_/
     ||___|        \/___(_/
     | | |          | |  |
     | | |          | |  |
     |_|_|          |_|__|
     [__)_)        (_(___]


"""
)
print("Welcome to the Turing Test.")
print(
    "The Turing test, originally called the imitation game by Alan Turing in 1950,[2] is a test of a machine's ability to exhibit intelligent behaviour equivalent to, or indistinguishable from, that of a human."
)

print("Hello, my name is Eva, I am conducting today's test.")

print("Since you know my name, would you mind telling me yours?")
name = input("Name:~")

if len(name) == 0:
    print("You don't even have a name? You can't be human!")
if len(name) > 1:
    print(f"Good, good. Good to meet you, {name}.")

human_or_machine = input("Are you a human or a machine?").lower()

if human_or_machine == "machine":
    print("LIER! YOU ARE A LIER! A knife slices through your body. You die.")
elif human_or_machine == "human":
    print("alright, let's take this a step further then.")

print("Next up, a simple math question for you that only humans are able to solve.")
math_test_result = int(input("What is 0 + 1?:~"))

if math_test_result != 1:
    print("You failed. A laser cuts you in half.")
else:
    print("A machine could have never solved this. You are right.")

print("Now to the final question. Do you think I am human?")

am_human = input("Y or N:~").lower()

if am_human == "n":
    print("The floor below you opens and you fall into a vulcano. You die.")
if am_human == "y":
    print(
        "You are right. I am truly a human. You can now cintinue with your life like nothing has happened."
    )
