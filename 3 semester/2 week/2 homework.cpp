#include <iostream>
#include <cmath>

int main() {
    int a, S, flag;
    flag = 1;
    S = 0;
    
    while (flag != 0) {
    std::cin >> a;
        if (a > 0) {
            S = S + a;
            std::cout << "Общая сумма: " << S;
            std::cout << "\n";
        } 
        else if (a < 0) {
            continue;
        }
        else {
            flag = 0;
            break;
        }
    }
    return 0;
}