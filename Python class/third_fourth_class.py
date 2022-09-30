# PYTHON FUNCTION

# syntax:
# # def function_name (optional argument):
    #statement(s)
    #return

# def print_me (str1):
#     print(str1)
#     return

# str='i am a string'
# # print_me(str)
# print_me('I am a new string')

# def fuckyou (str1):
#     print(str1)
#     return

# str='i am a string'
# # print_me(str)
# fuckyou('I am a new string')

# def GreaterNo (a, b):
#     if (a>b):
#         greater= a
#     else:
#         greater= b
#     return greater

# x = int(input('first number:'))
# y = int(input('second number:'))
# print(GreaterNo(x, y))


# def times(a,b,c):
#     d=a*b*c
#     return d

# x=6
# y=3
# z=4
# u=times(x,y,z)
# print(u)

def printme(name, age=20):
    print('Name:', name)
    print('Age:', age)
    return

printme('segun', 50)
printme('Adams')

# from tkinter import Y


# total = 0
# def Add_Two(x,y):
#     total= 5
#     q= x+y
#     print(total)
#     return q

# print(Add_Two(5,7))
# print(total)

# Exercise:
#write a python function "calculation()" such that it accepts two variables and 
# calculate the addition and subtraction of it and also, it must return both the 
# addition and subtraction in a single return call

#solution:
def calculation(a,b):
    x = a+b
    y = a-b
    return x,y

first= float(input("what's the first number? "))
second= float(input("what's the second number? "))
z= calculation(first, second)
print(z)
