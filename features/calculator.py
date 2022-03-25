from calculator_error import *


class Calculator():
    def __init__(self):
        self.numbers = []
        self.__result = 0
        self.__error = NoNumbersInsertedError()

    def insert(self, number):
        self.__error = EmptyError()
        self.numbers.append(number)

    def sum(self):
        if len(self.numbers) != 0:
            self.__result = sum(self.numbers)

    def multiply(self):
        if len(self.numbers) != 0:
            self.__result = 1
            for number in self.numbers:
                self.__result *= number

    def divide(self):
        if len(self.numbers) != 0:
            if self.numbers[-1] != 0:
                self.__result = self.numbers[-2] / self.numbers[-1] 
            else:
                self.__error = DivisionByZeroError()

    def result(self):
        self.numbers = []
        if not self.__error.thereIsError():
            result = self.__result
            self.__result = 0
            self.numbers = []
            self.__error = NoNumbersInsertedError()
            return result
        else:
            error = self.__error
            self.__error = NoNumbersInsertedError()
            return error

    def substract(self):
        if len(self.numbers) != 0:
            self.__result = self.numbers[0]
            for number in self.numbers[1:]:
                self.__result -= number
            self.numbers = []
