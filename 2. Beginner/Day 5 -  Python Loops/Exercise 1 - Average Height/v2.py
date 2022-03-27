student_count = 0
student_height_total = 0

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

    # get student heights and number of students from list via for loop, add them to student_count,
    # and student_height_total variables.
    student_height_total += student_heights[n]
    student_count += 1

# print (student_height_total)
# print (student_count)

# calculate using the average formula: sum of (heights/total student count)
average_height = student_height_total / student_count

# print with statement and make sure to use the [print(f"(statement+variable)".] to include variables.
print(f"The average height for this group of students is: {round(average_height)}cm.")
