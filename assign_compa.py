# Objective: The aim of this assignment is to get a grasp on how assignment operators work and
# how values can be compared using comparison operators. 

# Task1 - Value Swapping
# Swap the values of two given numbers using assignment operators (=) and then compare them to ensure they have been swapped.

num1 = 1    # Assigned first number with a value of 1
num2 = 24   # Assigned second number with a value of 24

swap = num1   # I created a third variable swap to contain the value of num1 which is 1. Thus swap is now = 1
num1 = num2   # This line will make num1 take num2 value. Thus, num1 value is now = 24
num2 = swap    # This will make num2 take swap value. Thus num2 value is now = 1

# Using comparison operators to confirm the swap below:

if num1 < num2:    # If num1 is less than num2, it means num1 value is still 1 and num2 value is still 24. Thus swap is unsuccessful.
    print("num1 is less than num2 which means the swap is unsuccessful")
if num1 > num2:   # If num1 is greater than num2, it means num1 value was changed to 24. Thus swap is a success.
    print ("num1 is greater than num2 which means the value of num1 is now 24. Swap is successful.")   


