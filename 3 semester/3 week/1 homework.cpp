#include <iostream>
#include <cmath>
#include <stdio.h>

#define N 8
#define flag true

void result_message(int *x) {
    for (unsigned j{}; j < N; j++)
    {
        x[j] = j*j;
        std::cout << "nums[" << j << "]: address=" << x+j
            << "\tvalue=" << *(x+j) << std::endl;
    }
}

int main() {
#if flag == true
    int nums[N] {};
#else
    int *nums {new int[N]{}};
#endif
     result_message(nums);
}