# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.
''' Afeera Firdoose M00979387'''

exam_one = int(input("Input exam grade one: "))

exam_two = int(input("Input exam grade two: "))# added int(

exam_3 = int(input("Input exam grade three: "))#changed str to int

grades = [exam_one, exam_two ,exam_3]# separated by commas, changed exam_three to exam_3
sum = 0
for grade in grades:# changed grade to gradea
  sum = sum + grade

avg = int(sum / len(grades))#corrected it to grades, taking integer value

if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg < 90:# added colon
    letter_grade = "B"
elif avg > 69 and avg < 80:
    letter_grade = "C"# changed quotes
elif avg <= 69 and avg >= 65:
    letter_grade = "D"
else: #changed elif to else
    letter_grade = "F"

# removed line (for grade in grades:)
print("Exams: " , grades[0],grades[1],grades[2])# changed to print all the grades

print("Average: " + str(avg))

print("Grade: " + letter_grade)

if letter_grade is "F":# changed - to _
    print ("Student is failing.")# added paranthesis 
else:
    print ("Student is passing.")# added paranthesis
    

