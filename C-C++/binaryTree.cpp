#include <iostream>
using namespace std;

int main()
{
    int num=5;
    // cin >> num;

    int zeroCount=0;
    for(int i=1;i<=num;i++)
    {
        if(i%2==0 || i%5==0)
            zeroCount+=1;
        if(i%10==0)
            zeroCount+=1;
        if(i%100==0)
            zeroCount+=1;
    }   
    cout << zeroCount <<"\n";
}