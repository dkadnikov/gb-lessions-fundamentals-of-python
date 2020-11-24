# Урок-4
# Задача-5

# Реализовать формирование списка, используя функцию range() и возможности генератора.
# В список должны войти четные числа от 100 до 1000 (включая границы).
# Необходимо получить результат вычисления произведения всех элементов списка.
# Подсказка: использовать функцию reduce().

# Решение-задачи-5
print("Решение-задачи-5")
print("")


from functools import reduce

def my_new_func(el_m, el):
    return el_m * el
''
#генерация четных значений
my_list = [el for el in range(99, 1001) if el % 2 == 0]
result = reduce(my_new_func, my_list)
print(f' Результат перемножения всех четных числе в массиве = {result}')
