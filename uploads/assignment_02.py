# Assignment 2: Check if a number is prime
# Write a function to check if a number is prime


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):  
        if n % i == 0:
            return False
    return True

# Test the function
num = 17
print(f"Is {num} prime? {is_prime(num)}")
print(f"Is 4 prime? {is_prime(4)}")
print(f"Is {undefined_var} prime?")  