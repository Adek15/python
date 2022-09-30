# Program to display price
# Accept price

# discount_price = 0
# price = float(input("Enter the price: "))
# if (price >= 50000):
#     discount_price = price*0.3
# elif (price >= 30000):
#     discount_price = price*0.2
# elif (price >= 10000):
#     discount_price = price*0.1
# amount= price-discount_price
# print('The amount to be paid is: '+ str(amount)) 
# else:
#     print('The amount to be paid is: '+ str(price))
#    (price > 50000):
#   discount_price = price*0.3


# Program to give discount and for only regular customers
# FT means first timers

price = float(input("Enter the price: "))
FT = input('Is the customer a first timer? (Y/N)? ')
amount = price
if (price >= 10000):
    if (FT == 'N'):
        discount = price*0.2
        amount = price-discount
    print ('The customer pays :'+ str(amount))