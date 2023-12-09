def break_time(scores):
    highest = lowest = scores[0]
    h = l = 0
    for x in scores:
        if x > highest:
            highest = x
            h += 1
        if x < lowest:
            lowest = x
            l += 1
    return [h, l]
