#include <valarray>

int rectangular(int s1, int s2, int s3)
{
    int c1 = (int) sqrt((s1 * s2) / s3);
    int c2 = s2 / c1;
    int c3 = s1 / c1;
    return (c1 + c2 + c3) * 4;

}