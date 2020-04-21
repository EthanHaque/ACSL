#include <bits/stdc++.h>

using namespace std;

bool isPrime(int n)
{
    for (int i = 0; i < floor(sqrt(n)); i++)
    {
        if (n % i == 0)
        {
            return false;
        }
    }
    return true;
}

bool isPSquare(int n)
{

}

int main()
{   
    int pieceLoc [6];
    int r;

    for (int i = 0; i < 6; i++)
    {
        cin >> pieceLoc[i];
    }
    sort(pieceLoc, pieceLoc + 6);
    cin >> r;

    for (int i = 0; i < r; i++)
    {
        int n;
        cin >> n;

        int temp0 = pieceLoc[0] + n;
        if (temp0 == pieceLoc[1])
        {
            continue;
        }
        else if (temp0 == 52)
        {
            pieceLoc[0] = 999;
        }
        else if (isPrime(temp0))
        {
            for (int i = 0; i < 6; i++)
            {
                if (temp0 < pieceLoc[1]-1)
                {
                    temp0++;
                }
            }
        }

        
        // if (pieceLoc[0] + n != pieceLoc[1])
        // {
        //     pieceLoc[0] += n
        // }
        // for (int j = 0; j < 6; j++)
        // {
        //     cout << pieceLoc[j] << " ";
        // }
        // cout << " \n";
    }

    
}