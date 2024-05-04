# The aim of this assignment is to get familiarized with basic arithmetic operations
# and understand how they can be applied in everyday situations.

# Task1 - Grocery Store Math
# Calculate the total cost of three items you'd commonly find in a grocery store, 
# given their individual prices. For example, what would be the cost of bread, 
# peanut butter, and jelly be? Prices don't need to be realistic

bread = 7.98            # Assigning a value (cost or price) to bread
peanut_butter = 6.49    # Assigning a value to peanut butter
jelly = 3.99            # Assigning a value to jelly

print(type(bread), type(peanut_butter),type(jelly))    
# I just wanted to see the type to make sure it's not a str otherwise the operation won't work.


total_cost = bread + peanut_butter + jelly
print("Grocery Total:", "$",total_cost)

print("==================================================================================")


# Task2 - Bank Interest
# If you have a savings account with a particular initial amount and a fixed yearly interest rate, 
# calculate the total amount in your account after a year. So if you had $10,000 at a 7% interest 
# write code that would tell us the amount at the end of the year. For the example the expected outcome would be $10,700.

savings_init = 10000
print(type(savings_init))   # Just checking to make sure it's an integer

annual_rate = 0.07    # 7% is converted in to decimal form
ytd = savings_init + (savings_init * annual_rate)
print(ytd)

savings_init2 = 50000    # If I had $50k in the bank
annual_rate2 = 0.1154    # If I was to invest in mutual funds. In 2022 the average was at 11.54%
ytd2 = savings_init2 + (savings_init2 * annual_rate2)
print("My total for $50K investment after a year at 11.54%:","$",ytd2)

gain = ytd2 - savings_init2
print("My realized gain:", "$",gain)


