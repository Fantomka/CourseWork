"""
Course project
This program should find a solution of linear algebraic equations system
using methods of Jordana-Gauss and Gauss-Seidel
"""

from random import randrange


class Matrix(list):
    def __init__(self, size=0):
        self.__dimension = size
        self.__coefficients = [[0 for element in range(size)] for row in range(size)]
        self.__answers = [0 for ans in range(size)]

    def get_coefficients(self) -> list:
        """
        :return: coefficients
        """
        return self.__coefficients

    def get_answers(self) -> list:
        """
        :return: answers
        """
        return self.__answers

    def get_extended_matrix(self) -> list:
        """
        :return: extended matrix
        """
        out = self.__coefficients
        out.append(self.__answers)
        return out

    def set_coefficients(self, coefs: list):
        """
        set coefficients list needs
        :param coefs: list of lists of coefficients
        :return:
        """
        self.__coefficients = coefs

    def set_answers(self, ans: list):
        """
        set answers, list needs
        :param ans: list of answers
        """
        self.__answers = ans

    def generate_rand_matrix(self, low=0, high=10):
        """
        generation random integer coefficients and answers
        :param low: left bound of the set
        :param high: right bound of the set
        """
        for line in range(self.__dimension):
            for column in range(self.__dimension):
                self.__coefficients[line][column] = randrange(low, high)
        self.__answers = [randrange(low, high) for el in range(self.__dimension)]

    def print_matrix(self):
        """
        simple printing matrix in command line
        """
        for line in self.__coefficients:
            for elem in line:
                print(f'{elem:<5}', end='')
            print()
        print()

    def print_extended_matrix(self):
        """
        simple printing extended matrix in command line
        """
        for line_index in range(self.__dimension):
            print('|', end='')
            for column_index in range(self.__dimension):
                print(f'{self.__coefficients[line_index][column_index]:^5}', end='')
            if self.__dimension // 2 is line_index:
                print(f'| = |{self.__answers[line_index]:^5}|')
            else:
                print(f'|   |{self.__answers[line_index]:^5}|')
        print()

    def swap_lines(self, index_1=0, index_2=0):
        """
        swapping lines
        :param index_1: index of line 1
        :param index_2: index of line 2
        """
        temp = self.__coefficients[index_1]
        self.__coefficients[index_1] = self.__coefficients[index_2]
        self.__coefficients[index_2] = temp

        temp = self.__answers[index_1]
        self.__answers[index_1] = self.__answers[index_2]
        self.__answers[index_2] = temp

    def adding_lines(self, addend_1, addend_2, number):
        """
        adding line 1 with line 2 multiplied on number
        result gets line 1
        :param addend_1: index line 1
        :param addend_2: index line 2
        :param number: coefficient
        """
        for elem_index in range(self.__dimension):
            self.__coefficients[addend_1][elem_index] += self.__coefficients[addend_2][elem_index] * number

        self.__answers[addend_1] += self.__answers[addend_2] * number



if __name__ == "__main__":
    while True:
        try:
            dimension = int(input("write dimension: "))
        except ValueError as er:
            print(er)
            continue
        else:
            break

    matr = Matrix(dimension)
    matr.generate_rand_matrix(0, 10)
    matr.print_extended_matrix()
    

