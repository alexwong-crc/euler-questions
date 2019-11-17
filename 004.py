# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers.

range1 = range(100, 1000)
range2 = range(100, 1000)

answer = 0


def isPalindrome(num):
    normal, reverse = [], []
    normal.extend(str(num))
    reverse = normal.copy()
    reverse.reverse()
    return normal == reverse


for num1 in range1:
    for num2 in range2:
        newNum = num1 * num2
        if isPalindrome(newNum) and newNum > answer:
            answer = newNum


print(answer)
