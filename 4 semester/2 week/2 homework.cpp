#include <iostream>
#include <map>
#include <string>

class PhoneBook {
private:
    std::map<std::string, std::string> Contacts;

public:
    void AddContact(const std::string& name, const std::string& phone) { // Функция добавления контакта
        Contacts[name] = phone;
    }

    void DeleteContact(const std::string& name) { // Функция удаления контакта
        if (Contacts.find(name) != Contacts.end()) {
            Contacts.erase(name);
        } else {
            std::cout << "The contact was not found. Cannot be deleted"<< std::endl;
        }
    }

    void FindContact(const std::string& name) { // Поиск контакта по имени (ключу)
        auto it = Contacts.find(name);
        if (it != Contacts.end()) {
            std::cout << "The contact was found: " << (*it).first << " " << (*it).second << std::endl;
        } else {
            std::cout << "The contact was not found"<< std::endl;
        }
    }

    void DispalyPhoneBook() { // Вывод телефонной книги
        if (Contacts.empty() == true) {
            std::cout << "The phone book is empty" << std::endl;
            return;
        }
        else {
            std::cout << "Contacts:" << std::endl;
            for (const auto& contact : Contacts) {
                std::cout << contact.first << ": " << contact.second << std::endl;
            }
        }
    }
};

int main() {
    PhoneBook NewPhoneBook;
    std::string name, phone;
    std::string task;
    bool finish_flag = true;

    std::cout << "phonebook commands" << std::endl;
        std::cout << "* Add *  add a new contact" << std::endl;
        std::cout << "* Delete *  delete a contact" << std::endl;
        std::cout << "* Search *  find a contact" << std::endl;
        std::cout << "* Display *  show the phonebook" << std::endl;
        std::cout << "* Finish *  finish the program" << std::endl;

    while (finish_flag == true) { // Реализация интерфейса через бесконечный цикл
        std::cout << "enter the command: ";
        std::cin >> task;
        
        if (task == "Add") {
            std::cout << "Enter the contact's name: ";
            std::cin >> name;
            std::cout << "Enter the contact's phone number: ";
            std::cin >> phone;
            NewPhoneBook.AddContact(name, phone);
        }
        else if (task == "Delete") {
            std::cout << "Enter the contact's name: ";
            std::cin >> name;
            NewPhoneBook.DeleteContact(name);
        }
        else if (task == "Search") {
            std::cout << "Enter the contact's name: ";
            std::cin >> name;
            NewPhoneBook.FindContact(name);
        }
        else if (task == "Display") {
            NewPhoneBook.DispalyPhoneBook();
        }
        else if (task == "Finish") {
            std::cout << "The program is closed" << std::endl;
            finish_flag = false;
        }
        else {
            std::cout << "Wrong command" << std::endl;
        }    
    }
}