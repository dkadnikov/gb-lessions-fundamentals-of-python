# Урок-6
# Задача-2
#  Реализовать класс Road (дорога), в котором определить атрибуты: length (длина), width (ширина).
#  Значения данных атрибутов должны передаваться при создании экземпляра класса.
#  Атрибуты сделать защищенными.
#  Определить метод расчета массы асфальта, необходимого для покрытия всего дорожного полотна.
#  Использовать формулу: длина * ширина * масса асфальта для покрытия одного кв метра дороги асфальтом,
#  толщиной в 1 см * чи сло см толщины полотна. Проверить работу метода.
#
# Например: 20м * 5000м * 25кг * 5см = 12500 т
#
# Решение-задачи-2
print("Решение-задачи-2")
print("")

class Road:
    def __init__(self, _lenght, _width, _mass, _thickness):
        self._lenght = _lenght
        self._width = _width
        self._mass = _mass
        self._thickness = _thickness

    def calculate(self):
        calculate = self._lenght * self._width * self._mass * self._thickness
        print(f'Вам потребуется {calculate} тонн асфальта для строительства дороги')

build_the_road = Road(20, 5000, 25, 0.005)
build_the_road.calculate()

