# Урок-3
# Задача-5

# Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме
# и после этого завершить программу.

# Решение-задачи-5
print("Решение-задачи-5")
print("")

# ДЛЯ ПРЕПОДОВАТЕЛЯ:
# Я НЕ СДЕЛАЛ ТАК, ЧТОБЫ МОЖНО БЫЛО ВВЕСТИ К ПРИМЕМУ "3Q" И ПРОГРАММА СЧИТАЛА
# У МЕНЯ СЧИТАЕТ ТОЛЬКО ЕСЛИ 3 и Q ВВЕДЕНЫ РАЗДЕЛЬНО

def imput_or_die():
    sum_res = 0
    exit = False
    while exit == False:
        number = input('Введите число или "Q" для выхода - ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == 'Q' or number[el] == 'Q':
                exit = True
                break
            else:
                res = res + int(number[el])
        sum_res = sum_res + res
        print(f'Сумма введенных чисел = {sum_res}')
    print(f'Итоговая сумма = {sum_res}')
imput_or_die()