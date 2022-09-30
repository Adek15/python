# Write a program to accept the cost price of a bike and display the amount to be paid after VAT 
# (value addedtax) has been added according to the following criteria: 
# Cost price (in Naira)            Tax 
# > 100000                         15 % 
# > 50000 and <= 100000            10% 
# <= 50000                         5%

#SOLUTION:

cost_price = float(input("what's the cost of the bike? "))
if (cost_price > 100000):
    VAT = cost_price * 0.15
elif (cost_price <= 100000 and cost_price > 50000):
    VAT = cost_price * 0.1
else:
    VAT = cost_price * 0.05
amount = cost_price + VAT
print ('The amount to be paid is', amount)