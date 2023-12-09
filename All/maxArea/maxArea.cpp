#include <vector>

int maxArea(std::vector<int> heights)
{
    int n = heights.size();
    std::vector<int> left, right;
    left.push_back(0);
    for (int i = 1; i < n; i++) 
        if (heights[i] > heights[left.back()])
            left.push_back(i);
    right.push_back(n - 1);
    for (int i = n - 2; i >= 0; i--) 
        if (heights[i] > heights[right.back()])
            right.push_back(i);
    int i = 0, j = 0, m = left.size() + right.size() - 2;
    int ans = 0, width, height;
    while (i + j <= m){
        width = right[j] - left[i];
        height = std::min(heights[left[i]], heights[right[j]]);
        ans = std::max(ans, width * height);
        if (heights[left[i]] > heights[right[j]]) 
            j++;
        else 
            i++;
    }
    return ans;
}