#include <iostream>
#include <random>
#include <chrono>

void quicksort(int *numbers, int size) { // Сама сортировка
        int i = 0;
        int j = size - 1;
        int mid = numbers[size / 2];
        do {
            //Пробегаем элементы, ищем те, которые нужно перекинуть в другую часть
            //В левой части массива пропускаем(оставляем на месте) элементы, которые меньше центрального
            while(numbers[i] < mid) {
                i++;
            }
            //В правой части пропускаем элементы, которые больше центрального
            while(numbers[j] > mid) {
                j--;
            }
            //Меняем элементы местами
            if (i <= j) {
                int a = numbers[i];
                numbers[i] = numbers[j];
                numbers[j] = a;
                i++;
                j--;
            }
        } while (i <= j);

        //Рекурсивные вызовы для окончательной сортировки
        if(j > 0) {
            //"Левый кусок"
            quicksort(numbers, j + 1);
        }
        if (i < size) {
            //"Правый кусок"
            quicksort(&numbers[i], size - i);
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

    quicksort(numbers, size);

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

// Время работы для 1000: 0.0001031, 0.0001012, 0.0000825 
// Среднее для 1000: 0,0000956
// Время работы для 5000: 0.0005662, 0.0009209, 0.0004322
// Среднее для 5000: 0,00064
// Время работы для 10000: 0.0017242, 0.0014124, 0.0009067
// Среднее для 10000: 0,001348