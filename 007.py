# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

# Method 1
# primeNumbers = []
# rangeList = list(range(2, 100))


# while len(primeNumbers) < 10001:
#     primeNumbers.append(rangeList[0])
#     rangeList = list(filter(lambda num: num % rangeList[0], rangeList))
#     if len(rangeList) <= 1:
#         rangeList.extend(list(range(rangeList[-1], rangeList[-1] + 1000, 2)))
#         for prime in primeNumbers:
#             rangeList = list(filter(lambda num: num % prime, rangeList))


# print(f"Prime numbers count: {len(primeNumbers)}")
# print(f"The 10001 prime number is: {primeNumbers[10000]}")


# Method 2
import math


def isPrime(number):
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    # for num in range(3, (number // 2) + 1, 2):
    for num in range(3, math.floor(math.sqrt(number)) + 1, 2):
        if number % num == 0:
            return False
    return True


value = 3
primes = [2]

while len(primes) < 10001:
    if isPrime(value):
        primes.append(value)
    value += 2

print(primes[-1])

