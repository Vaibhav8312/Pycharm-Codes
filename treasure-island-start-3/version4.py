print('''
 |--------------------------------------------------------------|
 |    ~-_____o___o____o____o_____o_____o____o____o____o_____-~  |
 |     ||~-______________________________________________-~||   |
 |     || |  __________________________________________  | ||   |
 |     || | ||||||                                |||||| | ||   |
 |     || | ||||||             |~\~|              |||||| | ||   |
 |     || | ||||||          (} |  \ ~~/           |||||| | ||   |
 |     || | ||||||          |__[~~~~~~~~)         |||||| | ||   |
 |     || |_||||||         [~]\~|~~~~|~~          ||||||_| ||   |
 |     |-~ . . . . . . . . . . . . . . . . . . . . . . .  ~||   |
 |    ~   . . . . . . . . . . . . . . . . . . . . . . . .    ~-_|
 |--------------------------------------------------------------|
''')
print("You are at a quiz show...")
print("Answer 3 questions to win 1 million imaginary dollars. Let's begin !!!")

question1 = input("What's the purpose of your life? Type 'to be happy' or 'to be a couch-potato'... Couch potato means a very lazy person (like me).\n")
question1_lower = question1.lower()

if question1_lower == "to be happy":
  print("Then you have a life (unlike me)... That's good !")
  question2 = input("Next question... Who do you see yourself in the future? Type 'a rich programmer' or 'a couch-potato homeless man'.\n ")
  question2_lower = question2.lower()
  if question2_lower == "a rich programmer":
    print("That's right... Good for you !!!")
    question3 = input("The last question is... What's mass measured in ? Type 'N' or 'kg'. ")
    question3_upper = question3.upper()
    if question3_upper == "N":
      print("Congratulations !!! You now have 1 million imaginary dollars you can do nothing with...")
    else:
      print("It's basic knowledge you learn at school !!! How do you want to be a rich programmer and live a happy life without knowing what is mass measured in? Shame on you...")
  else:
    print("What a lazy man (or woman) we have here... Ok, I need to stop to denigrate myself...")
else:
  print("You do not have a life. You do not deserve to win 1 million imaginary dollars !!! Life over for you !")
