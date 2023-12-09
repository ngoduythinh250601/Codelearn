#include <valarray>

int sumSquares(long long k)
{
    int ans = 0;
    for (long long i = 1; i*i <= k; i++){
        long long j = (int) sqrt(k - i*i);
        if (i*i + j*j == k) ans++;
    }
    return ans;
}