# Remove empty strings from the list of strings
# list1 =["Mike","","Emma","Kelly","","Brad"]

#Solution:

# list1 =["Mike","","Emma","Kelly","","Brad"]
# # del list1[1]
# # list1.remove("")
# list2 = [""]
# final_list = list(set(list1)-set(list2))
# print(final_list)


# list1 =["Mike","","Emma","Kelly","","Brad"]
# # list1.remove("")
# # list1.pop(1)
# # list1.pop()
# # del list1[1]
# # del list1
# # list1.clear()
# print(list1)

# names =["Mike","","Emma","Kelly","","Brad"]
# for i in range (len(names)):
#     print(names[i])
    
# names =["Mike","","Emma","Kelly","","Brad"]

# print(i for i in names)

# duplicate = [2, 4, 10, 20, 5, 2, 20, 4]
# print(list(set(duplicate)))

# names =["Mike","","Emma","Kelly","","Brad"]
# print(list(set(names)))

# list1=["Mike","","Emma","Kelly","","Brad"]
# for i in list1:
#     if (i == ""):
#     # del list1[i]
#         list1.remove(i)

# print(list1)

# list1.remove("")
# print(list1)
# list1.remove("")
# print(list1)


# Remove empty strings from the list of strings
# employee =["Mike","","Emma","Kelly","","Brad"]

# employee =["Mike","","Emma","Kelly","","Brad"]
# employee.remove('')
# employee.pop(4)
# del employee[2]
# print(employee)

# for i in employee:
#     if (i==''):
#         employee.remove(i)
# print(employee)

# for i in employee:
#     if i=='Mike' or i=='Brad':
#         employee.remove(i)
# print(employee)

#This should solve your first question:
item_list = ['item', 5, 'foo', 3.14, True]

for i in item_list:
    if i=='foo' or i==5 or i=='item' or i== True or i=='5':
        item_list.remove(i)
print("the rem value is %s"%(item_list))