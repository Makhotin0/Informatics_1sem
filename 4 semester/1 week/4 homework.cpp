#include <iostream>
#include <stack>
#include <string>

int main() {
    std::string line;
    std::cin >> line;
    std::stack<char> Stack; // Пользуемся стеком, чтобы потом проверять его на пустоту

    for (char it : line) { // В тупую перебор всех возможных случаев (были небольшие проблемы с выводом, но всё теперь работает верно)
        if (it == '(' or it == '{' or it == '[') { 
            Stack.push(it);
        } 
        else {
            if (Stack.empty()) {
                std::cout << "not correct";
                int n; // чтобы программа не заканчивалась и можно было посмотреть результат 
                std::cin >> n;
                return 0;
            }
            char last = Stack.top();
            if ((last == '(' and it == ')') or (last == '{' and it == '}') or (last == '[' and it == ']')) {
                Stack.pop();
            } 
            else {
                std::cout << "not correct";
                int n; // чтобы программа не заканчивалась и можно было посмотреть результат 
                std::cin >> n;
                return 0;
            }
        }
    }

    if (Stack.empty() == true) { // Финальная проверка
        std::cout << "the correct one";
    } else {
        std::cout << "not correct";
    }

    int n; // чтобы программа не заканчивалась и можно было посмотреть результат 
    std::cin >> n;
}