import math


class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color) if self.__is_valid_color(*color) else [0, 0, 0]
        self.__sides = (
            list(sides) if self.__is_valid_sides(*sides) else [1] * self.sides_count
        )
        self.filled = False

    # Проверка валидности цвета
    def __is_valid_color(self, r, g, b):
        return all(isinstance(c, int) and 0 <= c <= 255 for c in (r, g, b))

    # Проверка валидности сторон
    def __is_valid_sides(self, *sides):
        return (
            len(sides) == self.sides_count
            and all(isinstance(s, (int, float)) and s > 0 for s in sides)
        )

    # Геттеры и сеттеры
    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]
        else:
            print("Неверный цвет. Цвет не изменён.")

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)
        else:
            print("Неверные стороны. Стороны не изменены.")

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius**2)


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        # Формула Герона
        a, b, c = self.get_sides()
        s = len(self) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        side = sides[0] if sides and isinstance(sides[0], (int, float)) and sides[0] > 0 else 1
        super().__init__(color, *[side] * self.sides_count)

    def get_volume(self):
        side = self.get_sides()[0]
        return side**3


# Тестирование
circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())  # [55, 66, 77]
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())  # [222, 35, 130]

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())  # [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())  # [15]

# Проверка периметра (круга), это и есть длина:
print(len(circle1))  # 15

# Проверка объёма (куба):
print(cube1.get_volume())  # 216
