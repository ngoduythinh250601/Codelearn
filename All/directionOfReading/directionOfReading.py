def directionOfReading(numbers):
    n = len(numbers)
    a = ["{:0{}}".format(x, n) for x in numbers]
    return [int("".join([str(num[i]) for num in a])) for i in range(n)]
