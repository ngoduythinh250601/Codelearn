#include <string>

std::string generousMan(int n, int m)
{
    int van = 0, viet = 0;
    for (int i = 1; n >= i; n-=i, i+=2, van++);
    for (int i = 2; m >= i; m-=i, i+=2, viet++);
    return van <= viet ? "Van" : "Viet";
}