fibonacci = [1]
term = 2
i = 0
total = 0

while term < 4000000:
    if term % 2 == 0:
        total += term
    fibonacci.append(term)
    term = fibonacci[i] + fibonacci[i + 1]
    i += 1

print(total)
