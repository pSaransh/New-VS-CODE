#include<iostream>
using namespace std;

class Country{
    private: 
        string name;
        int populationCount;

    public: 
        Country(string s, int n){
            name = s;
            populationCount = n;
        }

        friend void getPopulationCount(Country);
};

void getPopulationCount(Country c){
    cout<<"Population Count: "<<c.populationCount;
}

int main(){
    Country c1 = Country("India", 130000000);
    getPopulationCount(c1);
    return 0;
}