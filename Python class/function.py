def total_calc(amount, tip):
    tip_perc = amount*(tip/100)
    total_amount = amount + tip_perc
    return total_amount

x= int(input("what's the total amount to be paid? "))
y= float(input("what's the tip percentage? "))

print(total_calc(x, y))
