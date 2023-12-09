def control_robot(start, directions):
    d = ["B", "DB", "D", "DN", "N", "TN", "T", "TB"]
    r = directions.count("P")
    return d[(d.index(start) + r - len(directions) + r) % 8]
