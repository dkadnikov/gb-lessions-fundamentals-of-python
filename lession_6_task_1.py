# Урок-6
# Задача-1

# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
#
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее сообщение и завершать скрипт.
#
# Решение-задачи-1
print("Решение-задачи-1")
print("")
from time import sleep

class TrafficLight:
    __colors = ['Красный', 'Желтый', 'Зеленый']

    def running(self):
        i = 0
        while i < 3:
            if i == 0:
                sleep(7)
                print(f'\033[31m {TrafficLight.__colors[i]}')
            elif i == 1:
                sleep(2)
                print(f'\033[33m\033[5m {TrafficLight.__colors[i]}')
            elif i == 2:
                sleep(5)
                print(f'\033[32m {TrafficLight.__colors[i]}')
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()