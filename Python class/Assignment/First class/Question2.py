# QUESTION: Write a program to check whether a number entered by user is even or odd.

# SOLUTION:

number = int(input ("What's the number? "))
if (number > 0):
    if (number%2)==0:
        print ("It's an even number")
    else: 
        print ("It's an odd number")
else:
    print ("It's not a positive number, hence, can't be either even or odd")