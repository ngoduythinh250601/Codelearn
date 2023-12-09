#include <vector>

const int MAX_N = 1e6 + 5;
int bit[MAX_N];

void update(int val){
    for (; val < MAX_N; val += val & (-val)) bit[val]++; 
}

int get(int val){
    int res = 0;
    for (; val; val -= val & (-val)) res += bit[val];
    return res;
}

int solve(std::vector<int> arr)
{
    int n = arr.size(), ans = 0;
    for (int i = n - 1; i >= 0; i--)
    {
        ans += get(arr[i]);
        update(arr[i] + 1);
    }
    return ans;
}