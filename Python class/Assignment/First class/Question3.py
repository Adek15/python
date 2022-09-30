# QUESTION: Write a program to display "Hello" if a number entered by user is a multiple of five, otherwise print "Bye".

# SOLUTION:
number = int(input ("What's the number? "))
if (number > 0):
    if (number%5)==0:
        print ("Hello")
    else: 
        print ("Bye")
else:
    print ("It's not a positive number, hence, can't be a multiple of 5")