def count_bits_prime(L, R):
    ans = 0
    nt = [0] * 21
    nt[2] = nt[3] = nt[5] = nt[7] = nt[11] = nt[13] = nt[17] = nt[19] = 1
    for i in range(L, R + 1):
        ans += nt["{:b}".format(i).count("1")]
    return ans
