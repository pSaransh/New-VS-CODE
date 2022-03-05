#include<iostream>
using namespace std;

class Country{
    public:
        string name;
        int populationCount;
    
    void storeCountryInformation(string s, int n){
        name = s;
        populationCount = n;
    }
    void printDetails(){
        cout << "Country: "<<name<< "\nPopulation: "<<populationCount<<"\n";
    }
};

int main(){
    Country c1; //object
    c1.storeCountryInformation("India", 1300000000);
    c1.printDetails();
    return 0;
}