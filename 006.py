# The sum of the squares of the first ten natural numbers is,

# 1^2 + 2^2 + ... + 10^2 = 385
# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)^2 = 55^2 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

TARGET_NUMBER = 100

rangeList = list(range(1, TARGET_NUMBER + 1))

squaredTotal = 0

for number in rangeList:
    squaredTotal += number ** 2

squaredSumTotal = sum(rangeList) ** 2

print(squaredSumTotal - squaredTotal)
