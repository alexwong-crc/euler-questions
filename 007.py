# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

primeNumbers = []
rangeList = list(range(2, 100))


while len(primeNumbers) < 10001:
    primeNumbers.append(rangeList[0])
    rangeList = list(filter(lambda num: num % rangeList[0], rangeList))
    if len(rangeList) <= 1:
        rangeList.extend(list(range(rangeList[-1], rangeList[-1] + 1000, 2)))
        for prime in primeNumbers:
            rangeList = list(filter(lambda num: num % prime, rangeList))


print(f"Prime numbers count: {len(primeNumbers)}")
print(f"The 10001 prime number is: {primeNumbers[10000]}")
