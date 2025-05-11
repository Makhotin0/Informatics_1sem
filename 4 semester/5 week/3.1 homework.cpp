#include <iostream>
#include <thread>
#include <algorithm>
#include <cstring> // для memcpy
#include <mutex>
#include <random>

using namespace std;

// Функция для сортировки части массива
void mergesort(int *numbers, int start, int end) {
	std::sort(numbers + start, numbers + end);
}

void merge_parts(int* numbers, int start, int mid, int end) {
    int* a = new int[end - start];
    int i = start, j = mid, k = 0;

    while (i < mid && j < end) {
        if (numbers[i] < numbers[j]) {
            a[k++] = numbers[i++];
        } else {
            a[k++] = numbers[j++];
        }
    }

    while (i < mid) {
        a[k++] = numbers[i++];
    }

    while (j < end) {
        a[k++] = numbers[j++];
    }

    // Копируем отсортированную часть обратно в исходный массив
    std::memcpy(numbers + start, a, (end - start) * sizeof(int));
    delete[] a;
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

    // Создаем и запускаем потоки для сортировки частей массива
    std::thread sort_threads[number_threads];

    for (int i = 0; i < number_threads; ++i) {
        int start = i * part_size;
        int end = std::min(start + part_size, size);
        sort_threads[i] = std::thread(mergesort, numbers, start, end);
    }

    for (int i = 0; i < number_threads; ++i) { // Завершаем потоки
        sort_threads[i].join();
    }

    // Последовательное слияние отсортированных частей
    int mid1 = part_size;
    int mid2 = std::min(2 * part_size, size);

    // Сливаем части вместе
    merge_parts(numbers, 0, mid1, mid2);
    if (mid2 < size) {
        merge_parts(numbers, 0, mid2, size);
    }

    std::cout << "New numbers: "; // Вывод
    for (int i = 0; i < size; i++) {
        std::cout << numbers[i] << " ";
    }

    int t; // чтобы программа не заканчивалась и можно было посмотреть результат 
    std::cin >> t;
}