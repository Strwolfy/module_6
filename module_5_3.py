class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.floors}"

    # Сравнение на равенство
    def __eq__(self, other):
        if isinstance(other, House):
            return self.floors == other.floors
        return False

    # Сравнение на неравенство
    def __ne__(self, other):
        return not self.__eq__(other)

    # Сравнение на меньше
    def __lt__(self, other):
        if isinstance(other, House):
            return self.floors < other.floors
        return False

    # Сравнение на меньше или равно
    def __le__(self, other):
        if isinstance(other, House):
            return self.floors <= other.floors
        return False

    # Сравнение на больше
    def __gt__(self, other):
        if isinstance(other, House):
            return self.floors > other.floors
        return False

    # Сравнение на больше или равно
    def __ge__(self, other):
        if isinstance(other, House):
            return self.floors >= other.floors
        return False

    # Увеличение этажей (сложение)
    def __add__(self, value):
        if isinstance(value, int):
            self.floors += value
            return self
        raise TypeError("Можно добавлять только целые числа.")

    # Реализация __radd__ через __add__
    def __radd__(self, value):
        return self.__add__(value)

    # Реализация __iadd__ через __add__
    def __iadd__(self, value):
        return self.__add__(value)


# Пример использования
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
