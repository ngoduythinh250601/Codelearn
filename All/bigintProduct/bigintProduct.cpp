#include <string>
#include <vector>

string bigintProduct(string a, string b)
{
    int len1 = a.size();
    int len2 = b.size();
    if (len1 == 0 || len2 == 0)
    return "0";

    vector<int> result(len1 + len2, 0);
    int i_n1 = 0;
    int i_n2 = 0;
    for (int i=len1-1; i>=0; i--, i_n1++)
    {
        int carry = 0;
        int n1 = a[i] - '0';
        i_n2 = 0;        
        for (int j=len2-1; j>=0; j--, i_n2++)
        {
            int n2 = b[j] - '0';
            int sum = n1*n2 + result[i_n1 + i_n2] + carry;
            carry = sum/10;
            result[i_n1 + i_n2] = sum % 10;
        }
        if (carry > 0)
            result[i_n1 + i_n2] += carry;
    }
    int i = result.size() - 1;
    while (i>=0 && result[i] == 0) i--;
    if (i == -1)
    return "0";
    string s = "";
    while (i >= 0)
        s += std::to_string(result[i--]);
    return s;
}