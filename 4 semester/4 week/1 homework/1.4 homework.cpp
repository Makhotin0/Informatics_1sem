#include <iostream>
#include <random>
#include <chrono>

void selectionsort(int *numbers, int size) {
    int i, j, min;
    for (i = 0; i < size - 1; i++) {
        // Нахождение минимального элемента в массиве
        min = i;
        for (j = i + 1; j < size; j++) {
            if (numbers[min] > numbers[j]) {
                min = j;
            }
        }
        // Обмен минимального элемента с текущим элементом
        int a = numbers[i];
        numbers[i] = numbers[min];
        numbers[min] = a;
    }
}

int main() {
    const int size = 10000;
    int numbers[size];

    // Генерация массива со случайными данными 
    std::random_device rd; 
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dist(0, 10000);

    // Заполнение массива
    for (int i = 0; i < size; ++i) {
        numbers[i] = dist(gen);
    }

    auto start = std::chrono::high_resolution_clock::now();

    selectionsort(numbers, size);

    auto end = std::chrono::high_resolution_clock::now(); // Время работы программы
    std::chrono::duration<double> time = end - start;
    std::cout << time.count() << std::endl;
    
    std::cout << "New numbers: "; // Вывод
    for (int i = 0; i < size; i++) {
        std::cout << numbers[i] << " ";
    }

    int t; // чтобы программа не заканчивалась и можно было посмотреть результат 
    std::cin >> t;
}

// Время работы для 1000: 0.0006831, 0.0008853, 0.0006283
// Среднее для 1000: 0.00073223
// Время работы для 5000: 0.0146459, 0.021019, 0.015486
// Среднее для 5000: 0.0170503
// Время работы для 10000: 0.0628681, 0.0617081, 0.0597297
// Среднее для 10000: 0.0614353
