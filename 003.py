# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143 ?


def isPrimeNumber(number):
    for num in range(2, (number // 2) + 1):
        if number % num == 0:
            return False
    return True


target = 600851475143
answer = 0

while target % 2 == 0:
    answer = 2
    target = target / 2


for x in range(3, (target // 2) + 1, 2):
    if isPrimeNumber(x):
        if target % x == 0:
            answer = x
            target = target / x
            if x > target:
                break

print(answer)

