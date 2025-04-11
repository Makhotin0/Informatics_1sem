#include <iostream>
#include <cmath>
#include <string>
using namespace std;

enum {s=10};

struct bookshelf {
    string book_name = "Неизвестно";
    struct author {
        string name_avtor;
        string surname_avtor;
    };
    int book_year = 0;
    int book_paper = 0;
    struct author avtor{"Неизвестно", "Неизвестно"};

    void createbook () {
        cout << "Название книги: ";
        cin >> book_name;
        cout << "Имя автора: ";
        cin >> avtor.name_avtor;
        cout << "Фамилия автора: ";
        cin >> avtor.surname_avtor;
        cout << "Год книги: ";
        cin >> book_year;
        cout << "Количество страниц: ";
        cin >> book_paper;
    }

     void displaybook () {
        cout << "Название книги: " << book_name << endl;
        cout << "Имя автора: " << avtor.name_avtor << endl;
        cout << "Фамилия автора: " << avtor.surname_avtor << endl;
        cout << "Год книги: " << book_year << endl;
        cout << "Количество страниц: " << book_paper << endl;
    }
};

int main() {
    struct bookshelf library[s];
    library[1].createbook();
    library[1].displaybook();
}