# Program to calculate sum of all prime numbers under 2 million
# author: Lisa Oh

from math import sqrt

# Function to check whether a number is prime
def is_prime(n):
    
    # If the number is less than 3, it is prime
    if (n <= 3):
        return True
    
    # Check to see if the number is divisible by any number starting from 2 to 
    for number in xrange(2,int(sqrt(n) +1)):
        if n%number == 0:
            return False
    return True


def sum_of_primes(number):

    sum = 0
    i = 2

    while i <= number:
        if is_prime(i):
            sum = sum + i
        i = i+1

    return sum


print sum_of_primes(100)
