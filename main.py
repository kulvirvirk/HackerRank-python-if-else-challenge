# Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Input Format

# A single line containing a positive integer, .

# Constraints

# Output Format

# Print Weird if the number is weird; otherwise, print Not Weird.


user_Integer = input('Enter a integer between 1 and 100::')
user_Integer = int(user_Integer)
while user_Integer < 1 or user_Integer > 100: 
  print("invalid input!")
  user_Integer = input('Enter a integer between 1 and 100:')
  user_Integer = int(user_Integer)


