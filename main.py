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


if user_Integer % 2 == 1:
  print('Weird')
elif user_Integer >= 2 and user_Integer <= 5: 
  print('Not Weird')
elif user_Integer >= 6 and user_Integer <= 20: 
  print('Weird')
elif user_Integer > 20: 
  print('Not Weird')