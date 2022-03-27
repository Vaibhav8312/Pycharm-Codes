print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

combined_names = name1 + name2
lower_names = combined_names.lower()

# t = lower_names.count("t")
# r = lower_names.count("r")
# u = lower_names.count("u")
# e = lower_names.count("e")
#
# true = t + r + u + e
#
# l = lower_names.count("l")
# o = lower_names.count("o")
# v = lower_names.count("v")
# e = lower_names.count("e")
#
# love = l + o + v + e
true = 0
love = 0
for letters in "true":
    true += lower_names.count(letters)
for letters in "love":
    love += lower_names.count(letters)

# if love > 9:
#     true += int(str(love)[0])
#     love = str(love)[1]
#     love = int(love)

# love_score = int(str(true) + str(love))

love_score = true * 10 + love

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif 40 <= love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
