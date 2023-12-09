int sumOfOddNumbers(int a, int b)
{
    a++, b--;
    if (a % 2 == 0) a++;
    if (b % 2 == 0) b--;
    return (1LL * (a + b) * ((b - a) / 2 + 1) / 2) % 10000007;
}