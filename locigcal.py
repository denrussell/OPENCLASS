# Exploring Logical Operations and Precedence
# Objective: The aim of this assignment is to grasp the concept of logical operations
# and understand how operator precedence can affect the outcome of an operation.

# Task1 - Validating Calculations
# Calculate the value of a particular arithmetic expression twice: once normally, 
# and once using parentheses. Compare the two results to see if they match.

val1 = 1232  # Assigning first value
val2 = 777   # Assigning the other value

result1 = val1 + val2   # normal operation. First result
print(result1) 

result2 = (val1 + val2) # using parenthesis. Second result
print(result2)

result = result1 == result2  # Comparing both results to see if they are equal or the same. True means equal.
print(result)

print("=======================================================================")
# Task 2 - Mix and Match
# Combine arithmetic (+), logical (or), and comparison (>) operators in a single expression
# and predict the outcome. Then, compute the expression to see if the prediction was correct.

# Comparison of two salaries with made up figures

hourly1 = 45
hourly2 = 70
bonus1 = 5000
bonus2 = 15000

biotech = hourly1 + bonus1       # Biotech salary plus bonus
softeng = hourly2 + bonus2       # Software Engineer salary plus bonus

decision_factor1 = biotech > softeng         # Setting up comparison if biotech earns more, True or False
print(decision_factor1)                      

decision_factor2 = softeng > biotech          # Setting up comparison if software engineer earns more, True or False
print(decision_factor2)

change_career = decision_factor1 or decision_factor2    # Utilizing or function, if any of them is True.
print("Both careers are rewarding and promising:", change_career)      # Prediction should say True because one of them is True





