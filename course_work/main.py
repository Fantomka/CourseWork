"""
Курсовой проект
По теме: разработка программы решения системы линейный уравнений:
    - методом Гаусса - Жордана
    - методом Гаусса - Зейделя
Язык: Python 3.7
Среда: PyCharm
Название программы: main.py
Разработал: Симаньков А.В.
Дата: 31.03.2019
Версия: v 1.0

Задание:
Разработать программу, решающее систему линейных алгебраических уравнений
методами Жордана - Гаусса и Гаусса - Зейделя

Описание алгоритма:
1)Создание объекта класса Matrix
2) Запрос исходных данных от пользователя
    а)Ввод пользователем размерности матрицы
    б)Ввод пользователем точности вычислений
    в)Ввод пользователем значений
3)Вывод построенной расширенной матрицы
4)Запрос выбора пользователем методом, которым будет решаться СЛАУ
5)Выввод результатов выполнения программы

Подпрограмма:
class_matrix.py - Класс матрица, хранящая в себе все необходимые данные и
весь необходимый функционал

Использованные переменные:
matrix - объект класса Matrix
answer - решение пользователя какой метод использовать
"""
from class_matrix import Matrix


if __name__ == '__main__':
    matrix = Matrix()
    matrix.set_size_user_mode()
    matrix.set_epsilon_user_mode()
    matrix.set_values_user_mode()
    #matrix.generate_rand_float_matrix(-100, 100)
    matrix.print_extended_matrix()
    done = False
    print("1 - метод Зейделя")
    print("2 - метод Жордана - Гаусса")
    while not done:
        answer = input("Выбирете метод (введите цифру): ")
        if answer == '1':
            for elem in matrix.gauss_seidel_method():
                print(f'X = {elem:^{matrix.epsilon + 5}.{matrix.epsilon}f}', end='')
            done = True
        elif answer == '2':
            for elem in matrix.jordana_gauss_method():
                print(f'X = {elem:^{matrix.epsilon + 5}.{matrix.epsilon}f}', end='')
            done = True
        else:
            print('Wrong answer, try again')
