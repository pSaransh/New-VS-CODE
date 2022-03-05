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
        friend class Continent;       
};

class Continent{
    private:
        string name;
        int totalCountries;

    public:
        Continent(string s, int n){
            name = s;
            totalCountries = n;
        }
        void getCountryPopulationCount(Country &c);   
};


void Continent::getCountryPopulationCount(Country &c){
    cout<<"Country Name: "<<c.name<<endl;
    cout<<"Population Count: "<<c.populationCount<<endl;
}

int main(){
    Country c1 = Country("India", 130000000);
    Continent n1 = Continent("Asia", 48);
    n1.getCountryPopulationCount(c1);
    return 0;
}