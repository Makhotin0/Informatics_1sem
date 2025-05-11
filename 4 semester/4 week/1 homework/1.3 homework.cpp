#include <iostream>
#include <random>
#include <chrono>

void merge(int* numbers,int start, int end, int mid, int size) {
	int merge_numbers[size];
	int i, j, k;
	i = start;
	k = start;
	j = mid + 1;
	
	while (i <= mid && j <= end) {
		if (numbers[i] < numbers[j]) {
			merge_numbers[k] = numbers[i];
			k++;
			i++;
		}
		else {
			merge_numbers[k] = numbers[j];
			k++;
			j++;
		}
	}
	
	while (i <= mid) {
		merge_numbers[k] = numbers[i];
		k++;
		i++;
	}
	
	while (j <= end) {
		merge_numbers[k] = numbers[j];
		k++;
		j++;
	}
	
	for (i = start; i < k; i++) {
		numbers[i] = merge_numbers[i];
	}
}

void mergesort(int *numbers, int start, int end, int size) {
	int mid;
	if (start < end){
        mid=(start+end)/2;
		mergesort(numbers, start, mid, size);
		mergesort(numbers, mid+1, end, size);
		merge(numbers, start, end, mid, size);
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

    mergesort(numbers, 0, size-1, size);

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

// Время работы для 1000: 0.0001393, 0.0001201, 0.0001098
// Среднее для 1000: 0.000123
// Время работы для 5000: 0.0006958, 0.0007717, 0.0009672
// Среднее для 5000: 0.0008116
// Время работы для 10000: 0.0011178, 0.0021529, 0.001529
// Среднее для 10000: 0.0015999