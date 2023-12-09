def findXORinacci(a, b, n):
    return a if n % 3 == 0 else b if n % 3 == 1 else a ^ b
