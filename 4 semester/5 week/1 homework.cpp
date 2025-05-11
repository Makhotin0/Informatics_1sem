#include <iostream>
#include <thread>
#include <mutex>

using namespace std;

mutex cout_mutex;

void print(int thread_id, int number_threads) // Вывод
{
    std::lock_guard<std::mutex> lock(cout_mutex);
    std::cout << "id thread: " << thread_id << " Number of threads: " << number_threads << " Message: HelloWorld\n" << std::endl;
}

int main() {
    int number_threads = 8; 

    std::thread threads[number_threads];

    for (int i = 0; i < number_threads; ++i) {
        threads[i] = std::thread(print, i, number_threads);
    }

    for (int i = 0; i < number_threads; ++i) { // Завершаем потоки
        threads[i].join();
    }

    int n; // чтобы программа не заканчивалась и можно было посмотреть результат 
    std::cin >> n;
}

// Вывод всегда отличается, так как потоки используют одни и теже ресурсы и имеют одинаковый доступ к консоли для вывода сообщений
// Исправил это проблему с помощью мьютекса