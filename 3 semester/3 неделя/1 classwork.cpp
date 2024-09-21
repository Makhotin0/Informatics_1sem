#include <iostream>

int main() {

    int x = 1, y = 2;
    int &rx = x, &ry = y;
    rx = ry;

    int x{ 5 };
    std::cout << x << '\n';
    std::cout << &x << '\n';
    std::cout << *(&x) << '\n';
    return 0;
}