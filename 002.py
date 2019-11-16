# First attempt
def firstAttempt():
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

    print("solution 1: ", total)


# Second Attempt
def secondAttempt():
    sequence = [1, 2]
    total = 0

    while sequence[-1] < 4000000:
        if sequence[-1] % 2 == 0:
            total += sequence[-1]
        newTerm = sequence[-1] + sequence[-2]
        sequence.append(newTerm)

    print("solution 2: ", total)


# A posted answer I liked
def postedAnswer():
    firstTerm = 1
    lastTerm = 2
    total = 0

    while lastTerm <= 4000000:
        if lastTerm % 2 == 0:
            total += lastTerm
        oldLastTerm = lastTerm
        lastTerm = lastTerm + firstTerm
        firstTerm = oldLastTerm

    print(total)


# firstAttempt()
secondAttempt()
# postedAnswer()
