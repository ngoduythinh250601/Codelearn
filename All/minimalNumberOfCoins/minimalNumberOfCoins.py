def minimalNumberOfCoins(coins, price):
    ans = 0
    for x in sorted(coins, reverse=True):
        ans += price // x
        price %= x
    return ans
