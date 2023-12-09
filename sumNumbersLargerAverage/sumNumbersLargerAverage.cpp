#include <vector>

int sumNumbersLargerAverage(std::vector<int> a)
{
    double average = 0;
    for (int x : a) average += x;
    average /= a.size();
    int ans = 0;
    for (int x : a) if (x > average) ans += x;
    return ans == 0 ? -1 : ans;
}