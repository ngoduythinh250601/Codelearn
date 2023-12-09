int multiplicationOfLuckynumber(long long n)
{
    int last = n % 10, first;
    while (n > 0) {
        if (n < 10) first = n;
        if (n % 10 == 4) return -1;
        n /= 10;
    }
    return first*last % 10 == 4 ? -1 : first*last;
}