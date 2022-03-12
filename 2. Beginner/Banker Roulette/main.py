import random

####  METHOD - 1 ####

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# Get the total number of items in list.
num_items = len(names)

# Generate random numbers between 0 and the last index.
random_person = random.randint(0, num_items - 1)

# Pick out random person from list of names using the random number.
person_who_will_pay = names[random_person]
print(person_who_will_pay + " is going to buy the meal today!")

##### METHOD - 2 #####

random.shuffle(names)

print(f"{names[0]} is going to buy the meal today!")

#### METHOD - 3 ####

import random

random_names = random.choice(names)
print(random.choices(names, k=2))

print(f"Today's bill will be paid by {random_names} !")

##### METHOD - 1 (SHORTER WAY) #####

import random

who_pay = random.randint(0, len(names) - 1)

print(f"{names[who_pay]} is going to buy the meal today!")
