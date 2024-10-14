#include <iostream>
#include <cmath>
#include <stdio.h>


int finder(int *x, int);
int finder(float *x, float);
int finder(char *x, char);

float F = 11.9; // то что ищем 
int N = 10; // размер массива
int main() {
    float nums[N] {1.3, 3.1, 4.5, 6.5, 0.9, 7.7, 9.1, 11.9, 5.4, 20.73}; // сам массив
    finder(nums, F);
}

int finder(int *x, int a) {
    for (unsigned j{}; j < N; j++)
    {
        if (x[j] == a) {
            std::cout << "nums[" << j << "]"; // позиция нужного символа 
            return 0;
        }
    }
    std::cout << "it has not been found";  
    return 0;
}

int finder(float *x, float a) {
    for (unsigned j{}; j < N; j++)
    {
        if (x[j] == a) {
            std::cout << "nums[" << j << "]"; // позиция нужного символа 
            return 0;
        }
    }
    std::cout << "it has not been found";  
    return 0;
}

int finder(char *x, char a) {
    for (unsigned j{}; j < N; j++)
    {
        if (x[j] == a) {
            std::cout << "nums[" << j << "]"; // позиция нужного символа 
            return 0;
        }
    }
    std::cout << "it has not been found";  
    return 0;
}