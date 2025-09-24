student_scores = input("Input a list of student scores \n").split()
# student_scores = "180 124 165 173 189 169 146".split()
highest_score = 0
for i in range(0, len(student_scores)):
    student_scores[i] = int(student_scores[i])
    if student_scores[i] > highest_score:
        highest_score = student_scores[i]

print(f"\nThe higest scores of the students is: {highest_score}")