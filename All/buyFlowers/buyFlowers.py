def buyFlowers(marigold, rose, m, n):
    return min(
        [rose * n, marigold * (n // m) + rose * (n % m), marigold * (n // m + 1)]
    )
