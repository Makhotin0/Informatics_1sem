#include <iostream>
#include <sstream>
#include <map>
#include <cctype>
#include <string>

int main() {
    std::string text;
    std::getline(std::cin, text); // Считывает весь текст (нельзя std::cin, т.к читает одно слово)

    for (auto it = text.begin(); it != text.end(); ++it) { // Удаление служебных символов
        if (std::ispunct(*it)) {
            *it = ' ';
        }
    }

    std::map<std::string, int> wordmap;
    std::string word;
    std::stringstream ss(text); // Всё, что выводится в такой поток, добавляется в конец строки; всё, что считыватся из потока — извлекается из начала строки. Из библиотеки iostream

    while (ss >> word) { // Извлечение данных из потока ss в переменную word (подсчёт слов с помощью словаря)
        wordmap[word]++;
    }

    int final_answer_number = 0;
    std::string final_answer_word;

    for (const auto& answer : wordmap) { // Находим самое самое распространённое слово
        if (final_answer_number < answer.second) {
            final_answer_number = answer.second;
            final_answer_word = answer.first;
        }
        else if (final_answer_number == answer.second) {
            if (final_answer_word > answer.first) {
                final_answer_word = answer.first;    
            }    
        }
        
    }

    std::cout << final_answer_word << ": " << final_answer_number << std::endl; 
    // apple, orange. banana\ banana: orange.

    int n; // чтобы программа не заканчивалась и можно было посмотреть результат 
    std::cin >> n;
}