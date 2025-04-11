#include <iostream>
#include <vector>

class spells
{
public:
	virtual void print() = 0;
};


class damage_spell : public spells
{
public:
	virtual void print()
	{
		std::cout << "A"<< std::endl;
	}
};


class buffing_spell : public spells
{
public:
	virtual void print()
	{
		std::cout << "B" << std::endl;
	}
};

class protection_spell : public spells
{
public:
	virtual void print()
	{
		std::cout << "C" << std::endl;
	}
};


class magic // Абстрактная фабрика 
{
public:
	virtual spells* create() = 0;
};

class damage_magic : public magic
{
public:
	virtual spells* create()
	{
		return new damage_spell;
	}
};

class buffing_magic : public magic
{
public:
	virtual spells* create()
	{
		return new buffing_spell;
	}
};

class protection_magic : public magic
{
public:
	virtual spells* create()
	{
		return new protection_spell;
	}
};

// компоновщик не получилось

int main()
{
	damage_magic* damage_page = new damage_magic{};
	buffing_magic* buffing_page = new buffing_magic{};
	protection_magic* protection_page = new protection_magic{};

	std::vector <spells*> spellbook;

	spellbook.push_back(damage_page->create());
	spellbook.push_back(buffing_page->create());
	spellbook.push_back(protection_page->create());

	for (auto i = 0; i < spellbook.size(); i++)
	{
		spellbook[i]->print();
	}
	
	for (auto i = 0; i < spellbook.size(); i++)
	{
		delete spellbook[i];
	}

	delete damage_page;
	delete buffing_page;
	delete protection_page;

	int n;
	std::cin >> n;
	return 0;
}