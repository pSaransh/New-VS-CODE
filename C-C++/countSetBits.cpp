#include <iostream>
using namespace std;

int main()
{
    int num=7;
    int setCount=0;
    while(num>0)
    {
        if((1&num)==1)
            setCount+=1;
        num=num>>1;
        //cout << num<<"\n";
    }
    cout<<setCount<<"\n";
}