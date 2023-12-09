#include <valarray>

bool richNumber(int n)
{
    long long sum = 1;
    if (n >= -1 && n <= 1) sum = 0;
    for (int i = 2; i <= (int) sqrt(n); i++)
        if (n % i == 0) {
            sum += i;
            int other = abs(n / i);
            if (i != other) sum += other;
        }
    return n < 0 ? false : sum > n;
}