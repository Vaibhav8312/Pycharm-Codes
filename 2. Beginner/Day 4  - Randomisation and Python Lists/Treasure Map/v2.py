row1 = ["⬜", "⬜", "⬜"]
row2 = ["⬜", "⬜", "⬜"]
row3 = ["⬜", "⬜", "⬜"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

position_selected = int(position)

column = int(position_selected / 10)
row = position_selected % 10

map[row - 1][column - 1] = "X"
print(f"{row1}\n{row2}\n{row3}")