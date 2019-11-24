# ex 1

today = input('What day is it?')

is_monday = (today == 'Monday')

print(is_monday)

print('Today is Monday: {}, this is my second argument {}'.format(is_monday, 'argument2'))

argument2 = 'SecondArgumentXPTO'
print(f'Today is Monday: {is_monday}, this is my second argument {argument2}')



#ex 2

price = input('What is the price of the gateaux?')

price_float = float(price)
print(price_float <= 10)
is_within_budget = (price_float <= 10)

print("Burger is within budget: {}".format(is_within_budget))


# ex 3

mars_choice = input('Would you like to visit Mars? y/n ')
is_willing = mars_choice == 'y'

affordable = input('Can you afford to visit Mars? y/n ')
can_afford = affordable == 'y'

should_visit_mars = (is_willing and can_afford)

print('You should visit Mars: {}'.format(should_visit_mars))


## ex 4

password = input('password: ')

if password == 'jumanji':
    print('Success!')
elif password == 'jumanjii':
    print('Almost!')
else:
    print('Try again!')



## ex 5

#Change Calculator

meal_price = float(input('How much was your meal?'))
member_card = input('Are you a member of our club?')

if meal_price >= 50:
    print('OMG you get 20% off!! Follow us on Tic-Tok')
    print('your bill is ' + str(meal_price*0.8) + '£')
elif meal_price >= 20:
    print('OMG you get 10% off!! Follow us on Tic-Tok')
    print('your bill is ' + str(meal_price*0.9) + '£')
else:
    print('next time you need to eat more :)')



##EX 6

    import random
    import time

    # ask for input
    user_input = float(input('heads or tails? - input 1 for heads, 2 for tails'))

    # flip coin
    coin_flip = random.randint(1, 2)

    # check user input vs coin flip
    # 1 equates to heads
    # 2 equates to tails

    if coin_flip == user_input:
        print('you win')
    else:
        print('you lose')