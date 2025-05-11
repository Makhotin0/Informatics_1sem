#include <iostream>
#include <thread>
#include <algorithm>
#include <mutex>
#include <random>

using namespace std;

void search_number(int *numbers, int target, int start, int end, bool *res, int id_thread, int *id_target) {
    bool answer = false;
    for (int i = start; i < end; ++i) {
        if (numbers[i] == target) {
            answer = true;
            res[id_thread] = answer;
            id_target[id_thread] = i;
            break;
        }
    }
}

int main() {
    const int size = 1000;
    int numbers[size];

    // Генерация массива со случайными данными 
    std::random_device rd; 
    std::mt19937 gen(rd());
    std::uniform_int_distribution<> dist(0, 1000);

    // Заполнение массива
    for (int i = 0; i < size; ++i) {
        numbers[i] = dist(gen);
    }

    const int number_threads = 3;
    int part_size = (size + number_threads - 1) / number_threads;

    // Создаем и запускаем потоки для поиска в массиве
    std::thread search_threads[number_threads];
    int target = 23;

    bool res[number_threads];
    int id_target[number_threads];
    for (int i = 0; i < number_threads; ++i) {
        res[i] = false;
        id_target[i] = -1;
    }
    
    for (int i = 0; i < number_threads; ++i) {
        int start = i * part_size;
        int end = std::min(start + part_size, size);
        search_threads[i] = std::thread(search_number, numbers, target, start, end, res, i, id_target);
    }

    // Ждем завершения всех потоков
    for (int i = 0; i < number_threads; ++i) {
        search_threads[i].join();
    }

    bool flag = false;
    for (int i = 0; i < number_threads; i++) {
        if (res[i] == true) {
            std::cout << "Found " << target << " Id: " << id_target[i];
            flag = true;
            break;
        }
    }

    if (flag != true) {
        std::cout << "Not found " << target;
    }

    int t; // чтобы программа не заканчивалась и можно было посмотреть результат 
    std::cin >> t;
}