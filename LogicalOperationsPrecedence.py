#Question 6 task 1 Validating Caluclations
# Calculate the value of a particular arithmetic expression twice: once normally, and once
# using parentheses. Compare the two results to see if they match.

x = 4 + 6 * 7 
y = (4 +6) * 7
is_true = x == y
print(x, y, is_true)

#Question 6 task 2 Mix and Match
# Combine arithmetic (+), logical (or) and comparison (>) operators in a single expression and
# predict the outcome. Then, compute the expression to see if the prediction was correct. 
a = 2
b = 5
c = 7
x = a + b * c > 0 & c < 30
y = (a + b) * c > 0 & c < 30
print(x, y)