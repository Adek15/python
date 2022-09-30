# Write a program to accept the cost price of a bike and display the road tax to be paid according 
# to the following criteria: 
# Cost price (in Naira)            Tax 
# > 100000                         15 % 
# > 50000 and <= 100000            10% 
# <= 50000                         5%

#SOLUTION:

cost_price = float(input("what's the cost of the bike? "))
if (cost_price > 100000):
    print('Road tax to be paid is 15%')
elif (cost_price <= 100000 and cost_price > 50000):
    print('Road tax to be paid is 10%')
else:
    print('Road tax to be paid is 5%')