#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>

int main() {

    std::map<std::string, std::string> name_tree;
    std::map<std::string, int> height_tree;
    std::set<std::string> read_set;

    std::ifstream infile("information.txt"); // Читаем файл
    int n;
    infile >> n;
    for (int i = 1; i < n; i++) { // Разбираем файл и добавляем родителей и потомков в map и set 
        std::string child, parent;
        infile >> child >> parent;
        name_tree[child] = parent;
        read_set.insert(child);
        read_set.insert(parent);
    }

    std::string first_parent; // Вычисление первого родителя
    for (const auto& name_child : read_set) {
        if (name_tree.find(name_child) == name_tree.end()) {
            first_parent = name_child;
            break;
        }
    }

    height_tree[first_parent] = 0; 

    std::vector<std::string> queue; // Обход дерева с подсчётом глубины (Использую обход в ширину)
    queue.push_back(first_parent);
    int head = 0;
    while(head < queue.size()) {
        std::string current = queue[head++]; 

        for(const auto& family : name_tree){
            if(family.second == current){
                std::string child = family.first;
                height_tree[child] = height_tree[current] + 1;
                queue.push_back(child);
            }
        }
    }

    std::vector<std::string> sort_name_tree; // Сортировка
    for (const auto& family : height_tree) {
        sort_name_tree.push_back(family.first);
    }
    std::sort(sort_name_tree.begin(), sort_name_tree.end());

    for (const auto& name : sort_name_tree) { // Вывод в консоль
        std::cout << name << " " << height_tree[name] << std::endl;
    }

    int t; // чтобы программа не заканчивалась и можно было посмотреть результат 
    std::cin >> t;
}