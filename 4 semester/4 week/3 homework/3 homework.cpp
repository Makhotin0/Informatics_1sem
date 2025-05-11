#include <iostream>
#include <random>
#include <chrono>

void optimizedquicksort(int *numbers, int size) { // Сама сортировка
    if (size <= 10) {
        int count = 0;
	    for(int i = 1; i < size; i++) {
		    for(int j = i; j > 0 && numbers[j-1] > numbers[j]; j--) {
			    count++;
			    int a = numbers[j-1];
			    numbers[j-1] = numbers[j];
			    numbers[j] = a;
		    }
	    }
    }
    else {
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
            optimizedquicksort(numbers, j + 1);
        }
        if (i < size) {
            //"Правый кусок"
            optimizedquicksort(&numbers[i], size - i);
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

    optimizedquicksort(numbers, size);

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