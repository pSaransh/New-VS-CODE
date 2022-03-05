#include<iostream>
using namespace std;

class Country{
    public:
        string name;
        int populationCount;
        static int countryCount;

    void setCountryDetails(string s, int n){
        this->name = s; // or name = s
        this->populationCount = n;
        countryCount++;
    }

    static int getTotalCountryCount(){
        return countryCount;
    }
};

int Country::countryCount = 0;

int main(){
    Country c1;
    c1.setCountryDetails("India", 1300000000);
    Country c2;
    c2.setCountryDetails("USA", 328200000);
    cout<<"Total Countries: "<<Country::getTotalCountryCount()<<endl;
}