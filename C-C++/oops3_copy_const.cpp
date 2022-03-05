
#include<iostream>
using namespace std;

class Country{
    public:
        string name;
        int populationCount;

    //Parameterized Counstructor
    Country(string s, int n){
        this->name = s; // or name = s
        populationCount = n; // or this->populationCount = n
    }

    void printCountryDetails(){
        cout<<"Country Name: "<<this->name<<endl;
        cout<<"Population Count: "<<this->populationCount<<endl;
    }
};

int main(){
    Country c1 = Country("India", 1300000000);
    Country c2 = c1;
    c2.printCountryDetails();
}