################### METHOD ########################

total = 0

for num in range(1, 101):
    if num % 2 == 0:
        total += num
print(total)

####################### METHOD 2 ########################

total2 = 0

for number in range(2, 101, 2):
    total2 += number
print(total2)

########################### METHOD 3 #########################

total = 0
for n in range(51):
    total += n

print(total * 2)
