# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

# Method 1

# def factor(number):
#     factorList = map(lambda x: number % x == 0, range(2, 21))
#     return all(factorList)


# number = 20

# while factor(number) == False:
#     print(number)
#     number += 20

# print(number)

# Method 2

MAX_NUMBER = 20
primeList = []


def addPrimeToList(numberList):
    primeList.append(numberList[0])
    newNumbers = list(filter(lambda x: x % numberList[0], numberList))
    if len(newNumbers) > 0:
        addPrimeToList(newNumbers)


addPrimeToList(list(range(2, MAX_NUMBER + 1)))


def findPrimeFactors(number):
    factors = []
    index = 0
    while number >= primeList[index]:
        if number % primeList[index] == 0:
            factors.append(primeList[index])
            number = number / primeList[index]
        else:
            index += 1
    return factors


factors = []

for x in range(2, MAX_NUMBER + 1):
    primeFactors = findPrimeFactors(x)
    if len(factors) == 0:
        factors.extend(primeFactors)
    for factor in factors:
        if factor in primeFactors:
            primeFactors.remove(factor)
    factors.extend(primeFactors)


answer = 1

for x in factors:
    answer = answer * x

print(answer)
