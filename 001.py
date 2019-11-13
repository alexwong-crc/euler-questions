maxNumber = 1000
numberToAdd = []
# multiples of 3 and 5
# sum all those numbers
for x in range(1, maxNumber):
    if( x % 3 == 0 or x % 5 == 0):
      numberToAdd.append(x)

print(sum(numberToAdd))