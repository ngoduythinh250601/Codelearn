#include <vector>
#include <math.h>

int maxSm(std::vector<std::vector<int>> inMatrix)
{
    int n = inMatrix.size(), m = inMatrix[0].size(), ans = 0;
    for (int i = 1; i < n; i++)
        for (int j = 1; j < m; j++)
            if (inMatrix[i][j])
            {
                inMatrix[i][j] += std::min(inMatrix[i][j-1], std::min(inMatrix[i-1][j], inMatrix[i-1][j-1]));
                ans = std::max(ans, inMatrix[i][j]);
            }
    return ans*ans;
}