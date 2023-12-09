def desktop_sorted(File, Memory, n):
    if len(File) == 0:
        return []
    if len(File) != len(Memory) or min(Memory) <= 0:
        return []
    item = [[Memory[i], File[i]] for i in range(len(File))]
    item.sort(reverse=(n % 2 == 1))
    return [x[1] for x in item]
