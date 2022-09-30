# Write a Python program to create the multiplication table (from 1 to 10) of a number. 

# Solution:

num = int(input("Multiplication table of what number? "))
for j in range (1, 11):
    print (num,'x',j,'=',num*j)