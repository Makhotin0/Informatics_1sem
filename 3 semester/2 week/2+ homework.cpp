#include <iostream>
#include <cmath>

int main() {
    unsigned n;
    std::cin >> n;
    int *numbers {new int[n]{}}; // выделяем память под массив

    delete[] numbers; // удаление массива 
}