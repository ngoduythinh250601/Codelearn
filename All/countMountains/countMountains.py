def count_mountains(A):
    return sum(A[i] > A[i - 1] and A[i] > A[i + 1] for i in range(1, len(A) - 1))
