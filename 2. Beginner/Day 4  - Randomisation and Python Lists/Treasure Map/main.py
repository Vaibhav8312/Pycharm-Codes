# "All things are difficult before they are easy" - Thomas Fuller
row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

selected_column = int(position[0])
selected_row = int(position[1])

map[selected_row - 1][selected_column - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")

#### ONE LINE SOLUTION ####
# map[int(position[1])-1][int(position[0])-1] ="x"
#


# 1. The user inputs a two-digit number (as a string) to represent the horizontal/vertical position of the treasure
#
# 2. We save the first index ([0]) of the inputted string to a new variable 'horizontal', which we'll use for the
# position going from left to right
#
# 3. We save the second index of the inputted string to a new variable 'vertical', which we'll use for the position
# going from top to bottom
#
# 4. We turn each string into an integer using the int function so we can use them as indeces
#
# horizontal = int(position[0])
# vertical = int(position[1])
# 5. We create a new variable called 'selected_column' that we equal to the value of 'vertical', passed as an index number to 'board'. This 'vertical' value tells us which of the three lists within the 'board' list of lists has been selected. e.g. an index value of '2' would be selecting the third - or bottom list - giving us our vertical (or column) position
#
# selected_column = board[vertical - 1]
# 6. We then get the index position of the individual item inside the selected list, which we mapped to the first digit in the user's input, remembering to subtract 1.
#
# 7. Lastly, we change the value of this item to the string "X" to mark the spot of the treasure!
#
# selected_column[horizontal - 1] = "X"
