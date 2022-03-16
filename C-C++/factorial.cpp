#include <iostream>
int factorial(int n){
    return n > 1 ? n*factorial(n-1) : 1;
}
int main(int argc, char const *argv[])
{
    std::cout << factorial(5);
    return 0;
}
