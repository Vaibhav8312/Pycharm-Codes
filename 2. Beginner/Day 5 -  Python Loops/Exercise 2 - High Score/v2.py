# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores: ").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])

# 🚨 Don't change the code above 👆

# Write your code below this row 👇

student_scores.sort()
print(student_scores)

# used the sort function to arrange the scores from lowest to highest or we can say in ascending order.
print(f"\nThe highest score in the class is: {student_scores[-1]}.")

# If you want to sort them in descending order, you can use the following line of code:
student_scores.sort(reverse=True)

for score in student_scores:
    if score == student_scores[-1]:
        print(f"\nThe highest score in the class is: \033[1m{score}\033[0m.")

