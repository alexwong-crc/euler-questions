# Method 1
# maxNumber = 1000
# numberToAdd = []
# for x in range(1, maxNumber):
#     if( x % 3 == 0 or x % 5 == 0):
#       numberToAdd.append(x)

# print(sum(numberToAdd))

# Method 2
total = 0
for n in range(1000):
    if n % 3 == 0 or n % 5 == 0:
        total = total + n

print(total)
