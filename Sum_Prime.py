# Program to calculate sum of all prime numbers under 2 million
# author: Lisa Oh

from math import sqrt


def is_prime(n):
    if (n <= 3):
        return True
    for number in xrange(2,int(sqrt(n) +1)):
        if n%number == 0:
            return False
    return True




print is_prime(25)
print is_prime(100)
print is_prime(3523)


def sum_of_primes(number):

    sum = 0
    i = 2

    while i <= number:
        if is_prime(i):
            sum = sum + i
        i = i+1

    return sum


print sum_of_primes(100)