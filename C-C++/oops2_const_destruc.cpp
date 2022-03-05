#include<iostream>
using namespace std;

class Country{
    public:
        string name;
        int populationCount;
    
    //Constructor
    Country(){
        cout<<"Country constructor envoked"<<endl;
    }

    //Destructor
    ~Country();

    //Parameterized Counstructor
    Country(string s, int n){
        this->name = s; // or name = s
        populationCount = n; // or this->populationCount = n
    }

    void storeCountryInformation(string s, int n){
        name = s;
        populationCount = n;
    }

    void printCountryDetails(){
        cout<<"Country Name: "<<this->name<<endl;
        cout<<"Population Count: "<<this->populationCount<<endl;
    }
};

Country::~Country(){
    cout<<"Destructor envoked"<<endl;
}

int main(){
    Country c1;
    c1.storeCountryInformation("India", 1300000000);
    c1.printCountryDetails();
    Country c2 = Country("USA", 327200000);
    c2.printCountryDetails();
    return 0;
}