"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
HIGHT_BONUS = 0.15
LOW_BONUS = 0.1


sales = float(input("Enter sales: $"))
while sales >= 0 :
    if sales < 1000 :
        bonus = sales * LOW_BONUS
    else:
        bonus = sales * HIGHT_BONUS
    print(f'bonus:{bonus}')
    sales = float(input("Enter sales: $"))
print("error")



