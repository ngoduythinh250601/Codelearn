#include <vector>
#include <string.h>

std::vector<int> disappearedNumbers(std::vector<int> a)
{
    int n = a.size();
    bool mark[n + 1];
    memset(mark, 0, sizeof mark);
    for (int x : a) mark[x] = true;
    std::vector<int> ans;
    for (int i = 1; i <= n; i++) if (!mark[i]) ans.push_back(i);
    return ans;
}