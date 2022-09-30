# Create a function showEmployee() in such a way that it should accept employee name 
# and its salary and display both and if the salary is missing in function, 
# call it should show it as 9000

# Solution:
# def showEmployee(employee_name, salary= 9000):
#     print(employee_name)
#     print (salary)
#     return 

# love= input('What is the employee name?: ')
# hate= int(input('What is the employee salary?: '))

# showEmployee(love, hate)
# showEmployee(love)

# Below does not return anything. it returns 'None'
# def showEmployee(employee_name, salary= 9000):
#     # print(employee_name)
#     # print (salary)
#     return 

# love= input('What is the employee name?: ')
# hate= int(input('What is the employee salary?: '))

# print(showEmployee(love, hate))
# print(showEmployee(love))



#Generate a python list of all the even numbers between 4 and 30
# print (list(range (4,31,2)))


# Reurn the largest item from the given list
#   aList = [4, 6, 8, 24, 12, 2]

aList = [4, 6, 8, 24, 12, 2]
aList.sort()
print(aList[-1])
