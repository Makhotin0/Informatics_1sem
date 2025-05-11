#include <iostream>
#include <random>
#include <chrono>

void bubblesort(int *numbers, int size) { // Сама сортировка
    for (int i = 0; i < size; i++) { 
        for (int j = 0; j < size-1; j++) {
            // меняем местами значения элементов
            if (numbers[j] > numbers[j + 1]) {
                int a = numbers[j];
                numbers[j] = numbers[j + 1]; 
                numbers[j + 1] = a; 
            }
        }
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

    bubblesort(numbers, size);

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

// Время работы для 1000: 0.0028705, 0.0020638, 0.0033695, 0.0029654, 0.0027298
// Среднее для 1000: 0.0027998
// Время работы для 5000: 0.0532787, 0.0525403, 0.051905, 0.053456, 0.049426
// Среднее для 5000: 0.0521212
// Время работы для 10000: 0.20398, 0.201269, 0.203346, 0.194386, 0.204013
// Среднее для 10000: 0.2013988