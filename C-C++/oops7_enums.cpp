
#include<iostream>
using namespace std;

enum Direction {North, South, East, West} dir;
enum Gender {Male, Female};

int main(){

    //Example 1
    dir = East;
    cout<<"Currenct Direction: "<<dir<<endl;
    //dir = NorthEast; //Error: identifier "NorthEast" is undefined
    for(int i= North; i<= West; i++){
        cout<<i<<" ";
    }
    cout<<endl;

    //Example 2
    Gender g = Male;
    cout<<"Gender: "<<g<<endl;
    switch (g)
    {
        case Male:
            cout<<"Male it is!"<<endl;
            break;
        case Female:
            cout<<"Female it is!"<<endl;
            break;
    }


    return 0;
}