def calc(steps, number):
    if number == root:
        return 0
    elif steps == 0:
        return 1
    elif (number - 1) % 3 == 0 and (number - 1) % 6 != 0:
        return calc(steps - 1, number * 2) + calc(steps - 1, (number - 1) // 3)
    else:
        return calc(steps - 1, number * 2)


def isaacRule(steps, number):
    if steps == 0:
        return 1
    global root
    root = number
    if (number - 1) % 3 == 0 and (number - 1) % 6 != 0:
        return calc(steps - 1, number * 2) + calc(steps - 1, (number - 1) // 3)
    else:
        return calc(steps - 1, number * 2)
