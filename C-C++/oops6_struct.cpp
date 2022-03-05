#include<iostream>
using namespace std;

struct Country{
    string name;
    int populationCount;

    Country(string s, int n){
        name = s;
        populationCount = n;
    }

    void showCountryDetails(){
        cout<<"Country Name: "<<name<<endl;
        cout<<"Country Population: "<<populationCount<<endl;
    }
};

int main(){
    struct Country c1 = Country("India", 1300000000);
    c1.showCountryDetails();
    return 0;
}