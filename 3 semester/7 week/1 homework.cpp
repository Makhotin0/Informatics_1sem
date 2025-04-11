#include <iostream>
#include <string>
#include <vector>

using namespace std;

class vet;

class animal
{
    friend class vet;
    protected:
        string name;
        string species;
        int age;
        int health;
    
    public:
        animal(string name, string species, int age, int health) : name(name), species(species), age(age), health(health) {}
        
        int data_animal()
        {
            std::cout << "name: " << name << ", species: " << species << ", age: " << age << ", health: " << health << endl;
            return 0;
        }

        virtual void makeSound() = 0;
};

class cat : public animal
{
    friend class vet;
    public :
        cat(string name, string species, int age, int health) : animal(name, species, age, health) {}
        
        void makeSound()
        {
            std::cout << "meow" << endl;
        }
};

class dog : public animal
{
    friend class vet;
    public:
        dog(string name, string species, int age, int health) : animal(name, species, age, health) {}
        
        void makeSound()
        {
            std::cout << "woof" << endl;
        }
};

class host
{
    friend class vet;
    private:
        string name;
        int age;
        int count_pets;
        
    public:
        host(string name, int age, int count_pets) : name(name), age(age), count_pets(count_pets) {}

        vector <animal*> pets; 
        
        int add_pets(animal* pet)
        {
            pets.push_back(pet);
            count_pets = count_pets + 1;
            return 0;
        }
        
        int data_host()
        {
            std::cout << "host: " << name << ", age: " << age << ", count_pets: " << count_pets << ", Pets: " << endl;
            for (auto pet : pets)
            {
                pet->data_animal();
            }
            return 0;   
        } 
};

class vet 
{
    public:

        int heal (animal& pet)
        {
            if (pet.health > 100) {
                std::cout << "The pet is in perfect health! " << endl;;
                pet.health = 100;
            }

            if (pet.health < 0) {
                std::cout << ":( " << endl;
                pet.health = 0;
            }

            else {
                std::cout << "Your pet is healthy! " << endl;
                pet.health = 100;
            }
            return 0;
        }

        int talk(host& Host)
        {
            std::cout << "Let's see what's wrong with your pet mister " << Host.name << endl;
            return 0;
        }
};

int main()
{
    cat* Cat = new cat("Barsik", "British", 10, 52);
    dog* Dog = new dog("Bobik", "Mongrel", 9, 60);

    Cat->makeSound();
    Dog->makeSound();
    
    host Host("Uncle Petya", 63, 0);
    Host.add_pets(Cat);
    Host.add_pets(Dog);
      
    Host.data_host();

    vet Vet;

    Vet.talk(Host);
    Vet.heal(*Cat);
    Vet.heal(*Dog);

    Host.data_host();
    
    delete Cat;
    delete Dog;
    
    int n;
    std::cin >> n;
    return 0;
}