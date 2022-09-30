# QUESTION:
# Write a program to check whether a person is eligible for voting or not. (accept age from user)

# SOLUTION:

# voting_age = 18
# age = int(input("What is the person's age? "))
# if (age >= voting_age):
#     print('The person is eligible for voting')
# else:
#     print('The person is not eligible for voting')

age = int(input("What is the person's age? "))
if (age >= 18):
    print('The person is eligible for voting')
else:
    print('The person is not eligible for voting')