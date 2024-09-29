#include <iostream>
#include <cmath>

int main() {
    int a, b;
    b = 0;
    std::cin >> a;

    for (int i = 2; i <= sqrt(a); i++) {
        if (a % i == 0) 
        {
            b = a / i;
            break;
        } 
        else 
        {
            continue;
        }
    }

    if (b != 0) {
        std::cout << "Наибольший делитель: " << b;
    }
    else {
        printf("Это простое число");
    }
    return 0;
}