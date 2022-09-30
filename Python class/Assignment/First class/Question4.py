# Write a program to calculate the electricity bill (accept number of unit from user) 
# according to the following criteria: 
#    Unit                   Price 
# First 100 units         no charge 
# Next 100 units          N5 per unit 
# After 200 units         N10 per unit 
# (For example, if input unit is 350 than total bill amount is N2000)

# SOLUTION:


unit = float(input("How many units have you consumed? "))
if (unit <= 100):
    amount = unit * 0
    print('no charge')
elif (unit <= 200):
    amount = (100*0)+(unit-100)*5
    print('total bill amount is #', amount)
else:
    amount = (unit-100)*0 + (200-100)*5 + (unit-200)*10
    print('total bill amount is #', amount)
