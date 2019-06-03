"""
Курсовой проект
По теме: разработка программы решения системы линейный уравнений:
    - методом главных элементов
    - методом разложения на произведение двух треугольных матриц
Язык: Python 3.7
Среда: PyCharm
Название программы: main.py
Разработал: Фомченков С.Д.
Дата: 31.03.2019
Версия: v 1.0

Задание:
Разработать программу, решающее систему линейных алгебраических уравнений
методам главных элементов и методом разложения на произведение двух треугольных матриц

Описание алгоритма:
1)инициализация системы
2)ввод данных
3)выбор метода
4)вывод результатов вычислений

Функции:
set_size - Ввод данных от пользователя
set_values - Ввод коэффициентов и свободных членов
generate_rand_matrix - генерирует случайные числа для коэффициентов и свободных членов в диапозоне
set_epsilon - Ввод точности вычисления и количество знаков после запятой в выводе
initialization - инициадизация системы
print_system - вывод системы
gauss_main_elem - метод главного элемента
multiply_line_by_number - Умножение строки на число
adding_lines - прибавляет к строке 1 строку 2, умноженную на число
LU_method - Метод разложения матрицы на произведение двух треуголььных матриц

Использованные переменные:
n - размерность матрицы
a - матрица коэффициентов
y - вектор свободных членов
epsilon - точность вычислений
answer - решение пользователя какой метод использовать
"""

from random import randrange


def set_size():
    """
    Ввод данных от пользователя
    """
    while True:
        try:
            n = int(input("Введите размерность матрицы, это целое число большее 1 и меньшее 7: "))
            if n <= 1 or n >= 7:
                continue
        except ValueError as error:
            print(error)
            continue
        else:
            return n


def set_epsilon():
    """
    Ввод точности вычисления и количество знаков после запятой в выводе
    """
    while True:
        try:
            eps = int(input('Задайте точность (количество чисел после запятой): '))
        except ValueError as error:
            print(error)
        else:
            break
    return eps


def initialization(size):
    a = [[0 for _ in range(size)] for _ in range(size)]  # инициализация
    y = [0 for _ in range(size)]
    return a, y


def set_values(size):
    """
    Ввод коэффициентов и свободных членов
    :param size: размер матрицы
    :return: ссылки на объекты a и y
    """
    for i in range(size):
        for j in range(size):
            while True:
                try:
                    a[i][j] = float(input(f'A[{i+1}, {j+1}]: '))
                    if a[i][j] < -50 or a[i][j] > 100:              # ОГРАНИЧЕНИЕ НА ВВОД
                        continue
                except ValueError as error:
                    print(error)
                    continue
                break
        while True:
            try:
                y[i] = float(input(f'Y[{i+1}, {size+1}]: '))
                if y[i] < -50 or y[i] > 100:                        # ОГРАНИЧЕНИЕ НА ВВОД
                    continue
            except ValueError as error:
                print(error)
                continue
            break
    return a, y


def generate_rand_matrix(a, y, n, low=0, high=10):
    """
    генерирует случайные числа для коэффициентов и свободных членов в диапозоне
    :param low: нижняя граница интервала
    :param high: верхняя граница интервала
    """
    for i in range(n):
        for j in range(n):
            a[i][j] = randrange(low, high)
    y = [randrange(low, high) for _ in range(n)]
    return a, y


def print_system(a, y, n):
    """
    Вывод матрицы
    """
    for i in range(n):
        for j in range(n):
            print(f'{a[i][j]}*x{j}', end='')
            if j < n-1:
                print(' + ', end='')
        print(f' = {y[i]}')
    print()


def gauss_main_elem(a, y, n, eps):
    x = [0 for _ in range(n)]
    eps = 1/(10**eps)  # точность
    k = 0
    while k < n:
        # поиск строки с максимальным a[i][k]
        maxi = abs(a[k][k])
        index = k
        for i in range(k+1, n):
            if abs(a[i][k]) > maxi:
                maxi = abs(a[i][k])
                index = i
        # Перестановка строк
        if maxi < eps:
            print("Решение получить невозможно из-за нулевого столбца ")
            print(index, " матрицы A")
            return 0
        for j in range(n):
            temp = a[k][j]
            a[k][j] = a[index][j]
            a[index][j] = temp
        temp = y[k]
        y[k] = y[index]
        y[index] = temp
        # Нормализация уравнений
        for i in range(k, n):
            temp = a[i][k]
            if abs(temp) < eps:
                continue  # для нулевого коэффициента пропустить
            for j in range(n):
                a[i][j] = a[i][j] / temp
            y[i] = y[i] / temp
            if i == k:
                continue  # уравнение не вычитать само из себя
            for j in range(n):
                a[i][j] = a[i][j] - a[k][j]
            y[i] = y[i] - y[k]
        k = k + 1
    # обратная подстановка
    for k in range(n-1, -1, -1):
        x[k] = y[k]
        for i in range(k):
            y[i] = y[i] - a[i][k] * x[k]
    return x


def multiply_line_by_number(a, y, line_index, number, n):
    """
    Умножение строки на число
    :param a: матрица коэффициентов
    :param y: список свободных членов
    :param line_index: номер строки
    :param number: число
    :param n: размерность матрицы
    """
    if number != 0:
        for elem_index in range(n):
            a[line_index][elem_index] *= number
        y[line_index] *= number
    else:
        print("Число не должно быть нулем")
    return a, y


def adding_lines(a, y, n, i1, i2, number):
    """
    прибавляет к строке 1 строку 2, умноженную на число
    """
    for j in range(n):
        a[i1][j] += a[i2][j] * number
    y[i1] += y[i2] * number
    return a, y


def LU_method(a, y, n):
    """
    Метод разложения матрицы на произведение двух треуголььных матриц
    :return: список неизвестных
    """
    print_system(a, y, n)
    for i in range(n):
        a, y = multiply_line_by_number(a, y, i, 1/a[i][i], n)
        for j in range(i+1, n):
            a, y = adding_lines(a, y, n, j, i, -a[j][i])
        for j in range(i-1, -1, -1):
            a, y = adding_lines(a, y, n, j, i, -a[j][i])
    return y


if __name__ == '__main__':
    n = set_size()
    epsilon = set_epsilon()
    a, y = initialization(n)
    #a, y = set_values(n)
    a, y = generate_rand_matrix(a, y, n, 11, 18)
    print_system(a, y, n)
    LU_method(a, y, n)
    print("1 - метод главных элементов")
    print("2 - метод разложения на произведение двух треугольных матриц")
    while True:
        chose = input("Выбирете метод (введите цифру): ")
        if chose == '1':
            for elem in gauss_main_elem(a, y, n, epsilon):
                print(f'X = {elem:^5.{epsilon}f}', end='')
            break
        elif chose == '2':
            for elem in LU_method(a, y, n):
                print(f'X = {elem:^5.{epsilon}f}', end='')
            break
        else:
            print('Некорректный ввод, попробуйте снова')
