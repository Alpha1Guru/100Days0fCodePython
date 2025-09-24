student_heights = input("Input a list of student heights \n").split()
# student_heights = "180 124 165 173 189 169 146".split()
num_of_students = 0
sum_of_students_heights = 0
for height in student_heights:
    sum_of_students_heights += int(height)
    num_of_students += 1
average_height = sum_of_students_heights / num_of_students
rounded_average_height = round(average_height)
print(f"\nThe average heights of the students is {rounded_average_height}")