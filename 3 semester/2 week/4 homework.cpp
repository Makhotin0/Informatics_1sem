#include <iostream>
#include <cmath>
#include<string>
using namespace std; 

int main() { // Русские символы string не учитывает ;(
    string a, b;
    std::cin >> a;
    std::cin >> b;
    int S = 0;

    for (int i = 0; i < size(a); i++) 
    {
        if (a[i] == b[0]) {
            for (int j = 0; j < size(b); ++j) 
            {
                if (a[i+j] == b[j] && (j+1) == size(b)) {
                    S = S + 1;
                }
                else if (a[i+j] != b[j]) {
                    break;
                }
            }
        }
    }
    std::cout << S;  
}