long long maxComNumbers(long long n)
{
    long long ans = n / 4;
    int r = n % 4;
    if (r % 2 == 1) ans--;
    return ans <= 0 ? -1 : ans;
}