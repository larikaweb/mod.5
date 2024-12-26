class House:
    def __init__(self,name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.number_of_floors}"

    def __len__(self):
        return self.number_of_floors

    def go_to(self, new_floor):
        if 1 <= new_floor <= self.number_of_floors:
            for floor in range(1, new_floor + 1):
                print(f"Проехали этаж {floor}")
        else:
            print("Такого этажа не существует")

h1 = House('ЖК Горский', 18)
print(h1)
h1.go_to(1)
h2 = House('Домик в деревне', 2)
print(h2)
h2.go_to(1)
