class Cat():
  def __init__(self, breed, color, age):
     self.breed = breed
     self.color = color
     self.age = age

  def meow(self):
     print('Мяу!')

first_cat = Cat('Абиссинская', 'Рыжая', 4)
for i in range(300):
    first_cat.meow()

