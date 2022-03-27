student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

# Because it is going to store the highest score, you should start with a value of zero
# (if you wanted to store the lowest score, you would start at 100 and replace > with < ).
# Then, for each student, see if their score is higher than the value in that variable. If it is, then store that
# student's score in the variable.
highest_score = 0

for score in student_scores:
    if score > highest_score:
        highest_score = score
print(f"The highest score in the class is: {highest_score}")


