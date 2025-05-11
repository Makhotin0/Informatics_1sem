#include <iostream>
#include <random>
#include <chrono>

void optimizedbubblesort(int *numbers, int size) { // Сама оптимизированная сортировка
    bool flag;
    for (int i = 0; i < size; i++) { 
        flag = false;
        for (int j = 0; j < size-1-i; j++) {
            // меняем местами значения элементов
            if (numbers[j] > numbers[j + 1]) {
                int a = numbers[j];
                numbers[j] = numbers[j + 1]; 
                numbers[j + 1] = a; 
                flag = true;
            }
        }
        if (flag == false) {
            break;
        }
    }
}

int main() {
    const int size = 25000;
    int numbers[size];

    // Генерация массива со случайными данными 
    std::random_device rd; 
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dist(0, 25000);

    // Заполнение массива
    for (int i = 0; i < size; ++i) {
        numbers[i] = dist(gen);
    }

    auto start = std::chrono::high_resolution_clock::now();

    optimizedbubblesort(numbers, size);

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

// Время работы для 500: 0.0007417, 0.0006706, 0.0004374, 0.0004612, 0.0004744
// Среднее для 500: 0.00055706
// Время работы для 1000: 0.001645, 0.0022468, 0.0013449, 0.0019688, 0.0022297
// Среднее для 1000: 0.00188704
// Время работы для 5000: 0.03283, 0.0324411, 0.0313472, 0.03487, 0.0336831
// Среднее для 5000: 0.03303428
// Время работы для 10000: 0.138204, 0.134133, 0.139784, 0.135931, 0.131274
// Среднее для 10000: 0.1358652
// Время работы для 25000: 1.11601, 1.10394, 1.11998, 1.12981, 1.12345
// Среднее для 25000: 1.118638