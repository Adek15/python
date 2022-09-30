# Write a program to accept percentage from the user and display the grade according to the following criteria: 
# Marks            Grade 
# > 90               A 
# > 80 and <= 90     B 
# >= 60 and <= 80    C 
# below 60           D

# SOLUTION:

marks = int(input("what's the student percentage mark? "))
if (marks > 90):
    grade = 'A'
elif (marks <= 90 and marks > 80):
    grade = 'B'
elif (marks <= 80 and marks >= 60):
    grade = 'C'
else:
    grade = 'D'
print ('Your garde is',grade)