# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def factor(number):
    factorList = map(lambda x: number % x == 0, range(2, 21))
    return all(factorList)


number = 20

while factor(number) == False:
    print(number)
    number += 20

print(number)

