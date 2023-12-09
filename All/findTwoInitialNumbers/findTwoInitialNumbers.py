def findTwoInitialNumbers(n, listOfDivisors):
    x = max(listOfDivisors)
    for i in range(1, x + 1):
        if x % i == 0:
            listOfDivisors.remove(i)
    return [x, max(listOfDivisors)]
