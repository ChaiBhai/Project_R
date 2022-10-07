#Project Y.E.T.M (You Eat Too Much)
def CTC(food_cost, tip_amount, tax_amount):
    total_amount = 0.00
    if food_cost < tip_amount:
        print('Have a nice day! But next time try to tip the waiter less money then you actually spend on food :)')
    else:
        print('Have a nice day!')
    total_amount = food_cost * (1 + (tax_amount / 100)) + tip_amount
    print('$' + str(total_amount) + ' has been taken from your card')
    print('---------------------------------------')

food_cost = 0
tip_amount = 0

print('Welcome to Y.E.T.M')
print('---------------------------------------')
food_cost= int(input('Food cost: '))
'''
food_cost is an integer
'''
tip_amount= int(input('Tip amount: '))
'''
The tip_amount is also an integer
'''

CTC(food_cost,tip_amount,6)



    
