#include <iostream>
#include <cmath>

int main() {
    unsigned n, S;
    S = 0;
    std::cin >> n;
    int nums[n] {}; 

    for (unsigned j{}; j < n; j++)
    {
        nums[j] = j*j;
        S = S + nums[j];
        std::cout << "nums[" << j << "]: address=" << nums+j
            << "\tvalue=" << *(nums+j) << std::endl;
    }

    std::cout << "Сумма элементов: " << S;
}