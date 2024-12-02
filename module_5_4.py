class House:
    # Атрибут класса для хранения истории зданий
    houses_history = []

    def __new__(cls, *args, **kwargs):
        # Добавляем название здания в историю
        if args:  # Проверяем, что args не пуст
            cls.houses_history.append(args[0])
        # Вызываем __new__ родительского класса, чтобы создать объект
        return super().__new__(cls)

    def __init__(self, name, floors):
        # Атрибуты объекта
        self.name = name
        self.floors = floors

    def __del__(self):
        # Сообщение при удалении объекта
        print(f"{self.name} снесён, но он останется в истории")


# Пример использования
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)

h2 = House('ЖК Акация', 20)
print(House.houses_history)

h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

# Проверка сохранённой истории
print(House.houses_history)
