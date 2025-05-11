#include <iostream>
#include <thread>
#include <ctime> 
#include <random>

using namespace std;

void addnumbers(int *numbers, int start, int end) { // Функция генерация чисел
    static std::mt19937 gen(std::random_device{}()); 
    std::uniform_int_distribution<int> dist(1, 1000);
    for (int i = start; i < end; ++i) {
        numbers[i] = dist(gen);
    }
}

int main() {
    const int size = 2000;
    int number_threads = 8;

    int numbers[size];
    std::thread threads[number_threads];

    // Разбиваем работу между потоками на области
    int part_size = size / number_threads;
    
    for (int i = 0; i < number_threads; ++i) {
        int start = i * part_size;
        int end;
    if (i == number_threads - 1) {
        end = size;
    } else {
        end = (i + 1) * part_size;
    }   
        threads[i] = std::thread(addnumbers, numbers, start, end);
    }

    for (int i = 0; i < number_threads; ++i) { // Завершаем потоки
        threads[i].join();
    }

    std::cout << "Numbers: "; // Вывод
    for (int i = 0; i < size; i++) {
        std::cout << numbers[i] << " ";
    }

    int t; // чтобы программа не заканчивалась и можно было посмотреть результат 
    std::cin >> t;
}