#include <iostream>
#include <iterator>
#include <string>
#include <list>

int main() { 
    std::list<int> Cont = {-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, 0, 1, 2, 3, 4, 5, 7, 6, 8, 9, 10, 3, 3, 4}; 

    std::list<int> PosCont; 
    std::list<int> NegCont;

    for (auto it = Cont.begin(); it != Cont.end(); ++it) { // Обощённый обход (сортировка по спискам, а также сортирует при добавлении)
        if (*it >= 0) { 
            auto Posit = PosCont.begin();
            while (Posit != PosCont.end() and *Posit < *it) {
                ++Posit;
            }
            PosCont.insert(Posit, *it);
            }

        if (*it <= 0) { 
            auto Negit = NegCont.begin();
            while (Negit != NegCont.end() and *Negit < *it) {
                ++Negit;
            }
            NegCont.insert(Negit, *it);
            }
    }

    for (auto it = Cont.begin(); it != Cont.end(); ++it) { // Вывод изначального списка
            std::cout << *it; 
        if (std::next(it) != std::end(Cont)) {  
            std::cout << ", ";  
        }
    }

    std::cout << "\n"; 

    for (auto it = PosCont.begin(); it != PosCont.end(); ++it) { // Вывод позитивного списка
            std::cout << *it; 
        if (std::next(it) != std::end(PosCont)) {  
            std::cout << ", ";  
        }
    }

    std::cout << "\n"; 

    for (auto it = NegCont.begin(); it != NegCont.end(); ++it) { // Вывод отрицательного списка
            std::cout << *it; 
        if (std::next(it) != std::end(NegCont)) {  
            std::cout << ", ";
        }
    }

    int n; // чтобы программа не заканчивалась и можно было посмотреть результат 
    std::cin >> n;
}