#include <iostream>
#include <iterator>
#include <string>
#include <vector>

template <typename Container> 
void Print(const Container& cont, const std::string& sign) { // Объявляем функцию, работающую с общими типами контейнеров 
    for (auto it = cont.begin(); it != cont.end(); ++it) { // Обощённый обход (конструкция из лекции)
        std::cout << *it; 
        if (std::next(it) != std::end(cont)) { // проверка на конец контейнера 
            std::cout << sign;  
        }
    }
    std::cout << "\n"; 
};

int main() {
    std::vector<int> V_Cont = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    Print(V_Cont, ", "); 
    int n; // чтобы программа не заканчивалась и можно было посмотреть результат 
    std::cin >> n;
}