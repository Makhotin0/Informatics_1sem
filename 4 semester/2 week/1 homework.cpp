#include <iostream>
#include <deque>
#include <string>

class Task { // Класс задачи
public:
    std::string Problem;
    bool Priority;

    Task(const std::string& problem, bool priority){ // Конструктор класса Task
        Problem = problem;
        Priority = priority;
    }  
};

class TaskDeque { // Класс контейнера
private:
    std::deque<Task> Deque;
public:
    void AddTask(const std::string& problem, bool priority) { // функция добавления задач в контейнер 
        Task newTask(problem, priority);
        if (priority == true) {
            Deque.push_front(newTask); 
        } else {
            Deque.push_back(newTask); 
        }
    }

    void DoingTask() { // функция выполнения задач в контейнер
        if (Deque.empty() == true) {
            std::cout << "All tasks are done" << std::endl;
            return;
        }

        Task LastTask = Deque.front();
        Deque.pop_front();

        std::cout << "The task is completed: " << LastTask.Problem << std::endl;
    }

    void SizeDeque() { // функция определения размера контейнера
        if (Deque.size() != 0) {
            std::cout << "Size of Deque: " << Deque.size() << std::endl;
        } 
        else {
            std::cout << "The Deque is empty" << std::endl;
        }
    }
};

int main() {
    TaskDeque NewTaskDeque;

    NewTaskDeque.AddTask("The first priority task", true);
    NewTaskDeque.AddTask("The first non-priority task", false);
    NewTaskDeque.AddTask("The second non-priority task", false);
    NewTaskDeque.AddTask("The third non-priority task", false);
    NewTaskDeque.AddTask("The second priority task", true);
    
    NewTaskDeque.SizeDeque();

    NewTaskDeque.DoingTask();
    NewTaskDeque.DoingTask();
    NewTaskDeque.DoingTask();
    NewTaskDeque.DoingTask();
    NewTaskDeque.DoingTask();

    NewTaskDeque.SizeDeque();
    NewTaskDeque.DoingTask();

    int n; // чтобы программа не заканчивалась и можно было посмотреть результат 
    std::cin >> n;
}