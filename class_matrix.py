"""
Course project
This program should find a solution of linear algebraic equations system
using methods of Jordana-Gauss and Gauss-Seidel
"""

from random import randrange, uniform
from math import sqrt


class Matrix(list):
    """
    This class using for collect information and methods about
    systems of linear algebraic equations and this class
    inheritance methods from class list
    """
    def __init__(self, size=0):
        """
        Initialization of matrix
        :param size: dimension of quadratic matrix
        """
        self.__dimension = size
        self.coefficients = [[0 for _ in range(size)] for _ in range(size)]
        self.answers = [0 for _ in range(size)]
        self.epsilon = 1

    def get_coefficients(self) -> list:
        """
        :return: coefficients
        """
        return self.coefficients

    def get_answers(self) -> list:
        """
        :return: answers
        """
        return self.answers

    def get_extended_matrix(self) -> list:
        """
        :return: extended matrix with coefficients and answers
        (list[dimension+1][dimension])
        """
        out = self.coefficients
        out.append(self.answers)
        return out

    def set_size_user_mode(self):
        """
        write invitation to set dimension of matrix
        """
        while True:
            try:
                self.__dimension = int(input("Write dimension, it should be integer and more then 1 and less then 7: "))
                if self.__dimension <= 1 or self.__dimension >= 7:
                    continue
            except ValueError as error:
                print(error)
                continue
            else:
                self.coefficients = [[0 for _ in range(self.__dimension)] for _ in range(self.__dimension)]
                self.answers = [0 for _ in range(self.__dimension)]
                break

    def set_values_user_mode(self):
        for line in range(self.__dimension):
            for column in range(self.__dimension):
                while True:
                    try:
                        self.coefficients[line][column] = float(input(f'   Matrix[{line+1}, {column+1}]: '))
                    except ValueError as error:
                        print(error)
                        continue
                    break
            while True:
                try:
                    self.answers[line] = float(input(f'Matrix[{line+1}, {self.__dimension+1}]: '))
                except ValueError as error:
                    print(error)
                    continue
                break

    def set_epsilon_user_mode(self):
        """
        set number of digits after pointer
        """
        while True:
            try:
                self.epsilon = int(input('Set accuracy (number of digits after point): '))
            except ValueError as error:
                print(error)
            else:
                break

    def set_coefficients(self, coefs: list):
        """
        set coefficients list needs
        :param coefs: list of lists of coefficients
        :return:
        """
        self.coefficients = coefs

    def set_answers(self, ans: list):
        """
        set answers, list needs
        :param ans: list of answers
        """
        self.answers = ans

    def generate_rand_integer_matrix(self, low=0, high=10):
        """
        generation random integer coefficients and answers
        :param low: left bound of the set
        :param high: right bound of the set
        """
        for line in range(self.__dimension):
            for column in range(self.__dimension):
                self.coefficients[line][column] = randrange(low, high)
        self.answers = [randrange(low, high) for _ in range(self.__dimension)]

    def generate_rand_float_matrix(self, low=0, high=10):
        """
        generation random integer coefficients and answers
        :param low: left bound of the set
        :param high: right bound of the set
        """
        for line in range(self.__dimension):
            for column in range(self.__dimension):
                self.coefficients[line][column] = round(uniform(low, high), self.epsilon)
        self.answers = [round(uniform(low, high), self.epsilon) for _ in range(self.__dimension)]

    def print_matrix(self):
        """
        simple printing matrix of coefficients in command line
        """
        for line in self.coefficients:
            for elem in line:
                print(f'{elem:<{self.epsilon + 2}.{self.epsilon}f}', end='')
            print()
        print()

    def print_extended_matrix(self):
        """
        simple printing extended matrix in command line
        """
        for line_index in range(self.__dimension):
            print('|', end='')
            for column_index in range(self.__dimension):
                print(f'{self.coefficients[line_index][column_index]:^{self.epsilon + 5}.{self.epsilon}f}', end='')
            if self.__dimension // 2 is line_index:
                print(f'| = |{self.answers[line_index]:^{self.epsilon + 5}.{self.epsilon}f}|')
            else:
                print(f'|   |{self.answers[line_index]:^{self.epsilon + 5}.{self.epsilon}f}|')
        print()

    def swap_lines(self, index_1=0, index_2=0):
        """
        swapping lines (coefficients and answers)
        :param index_1: index of line 1
        :param index_2: index of line 2
        """
        temp = self.coefficients[index_1]
        self.coefficients[index_1] = self.coefficients[index_2]
        self.coefficients[index_2] = temp

        temp = self.answers[index_1]
        self.answers[index_1] = self.answers[index_2]
        self.answers[index_2] = temp

    def swap_columns(self, index_1=0, index_2=0, ans_swap=False):
        """
        This method swaps columns in matrix
        :param index_1: index of first column
        :param index_2: index of second column
        :param ans_swap: bool variable. If it's True, swapping first column with column of answers
        """
        if ans_swap:
            for i in range(self.__dimension):
                temp = self.coefficients[i][index_1]
                self.coefficients[i][index_1] = self.answers[i]
                self.answers[i] = temp
        else:
            for i in range(self.__dimension):
                temp = self.coefficients[i][index_1]
                self.coefficients[i][index_1] = self.coefficients[i][index_2]
                self.coefficients[i][index_2] = temp

    def adding_lines(self, addend_1, addend_2, number):
        """
        adding line 1 with line 2 multiplied on number
        result gets line 1
        :param addend_1: index line 1
        :param addend_2: index line 2
        :param number: coefficient
        """
        for elem_index in range(self.__dimension):
            self.coefficients[addend_1][elem_index] += self.coefficients[addend_2][elem_index] * number
        self.answers[addend_1] += self.answers[addend_2] * number

    def multiply_line_by_number(self, line_index, number):
        """
        multiply line by number
        :param line_index: index of line
        :param number: value of number
        """
        if number != 0:
            for elem_index in range(self.__dimension):
                self.coefficients[line_index][elem_index] *= number
            self.answers[line_index] *= number
        else:
            print("number should not be zero")

    def set_not_zero_diagonal_element(self, index=0):
        """
        check in first line first element, if it is zero,
        tries to swap with line that have not zero element in first place
        """
        if self.coefficients[index][index]:  # check is elem != 0
            return
        for line_index in range(index + 1, len(self.coefficients)):
            if self.coefficients[line_index][index]:
                self.swap_lines(index, line_index)
                break
            else:
                continue

    def jordana_gauss_method(self):
        """
        this method tries to find list of roots of the equation
        Using Jordana-Gauss method
        After using this method matrix will become unit matrix
        :return: list of roots of the equation
        """
        for diagonal_index in range(self.__dimension):
            self.set_not_zero_diagonal_element(diagonal_index)
            self.multiply_line_by_number(diagonal_index, 1/self.coefficients[diagonal_index][diagonal_index])
            for under_index in range(diagonal_index + 1, self.__dimension):
                self.adding_lines(under_index, diagonal_index, -self.coefficients[under_index][diagonal_index])
            for upper_index in range(diagonal_index - 1, -1, -1):
                self.adding_lines(upper_index, diagonal_index, -self.coefficients[upper_index][diagonal_index])
        return self.answers

    def gauss_seidel_method(self):
        """
        this method tries to find list of roots of the equation
        Using gauss_seidel method
        converge - condition for terminating the computation of the system according to the seidel
        current: list of x values on current step
        previous: list of x values on previous step
        :return: list of roots of the equation
        """
        n = self.__dimension
        previous = [.0 for _ in range(n)]

        converge = False
        while not converge:
            current = previous[:]
            for line in range(n):
                sum1 = sum(self.coefficients[line][column] * current[column] for column in range(line))
                sum2 = sum(self.coefficients[line][column] * previous[column] for column in range(line+1, n))
                current[line] = (self.answers[line] - sum1 - sum2) / self.coefficients[line][line]
            converge = sqrt(sum((current[line] - previous[line]) ** 2 for line in range(n))) <= 1/(10 ** self.epsilon)
            previous = current[:]
        return previous
