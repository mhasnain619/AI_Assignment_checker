# Assignment 1: Calculate the factorial of a number
# Write a function to compute the factorial of a given number n
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Test the function
number = 5
result = factorial(number)
print(f"Factorial of {number} is {result}")