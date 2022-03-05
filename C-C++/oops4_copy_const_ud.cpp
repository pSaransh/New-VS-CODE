#include<iostream>
using namespace std;

class Country{
    public:
        string name;
        int populationCount;
        int *stateCount;

    Country(){
        stateCount = new int; //dynamically allocate memory for an integer and return it's address
    }

    //User defined copy constructor
    Country(Country &c){
        name = c.name;
        populationCount = c.populationCount;
        stateCount = new int; //dynamically allocate memory for an integer and return it's address
        *stateCount = *(c.stateCount);
    }

    void setCountryDetails(string s, int n, int count){
        this->name = s; // or name = s
        populationCount = n; // or this->populationCount = n
        *stateCount = count;
    }

    void printCountryDetails(){
        cout<<"Country Name: "<<this->name<<endl;
        cout<<"Population Count: "<<this->populationCount<<endl;
        cout<<"State Count: "<<*stateCount<<endl;
    }
};

int main(){
    Country c1;
    c1.setCountryDetails("India", 1300000000, 28);
    Country c2 = c1;
    int num = 29;
    c2.stateCount = &num;
    cout<<"C2"<<endl;
    c2.printCountryDetails();
    cout<<"C1"<<endl;
    c1.printCountryDetails();
}