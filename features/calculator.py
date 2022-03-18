class Calculator():
    def __init__(self):
        self.numbers = []
        self.__result = 0
    
    def insert(self, number):
        self.numbers.append(number)
    
    def sum(self):
        self.__result = sum(self.numbers)
        self.numbers = []

    def multiply(self):
        self.__result = 1
        for number in self.numbers:
            self.__result *= number
        self.numbers = []

    def divide(self):
        self.__result = self.numbers[-2] / self.numbers[-1] 
        self.numbers = []

    def result(self):
        result = self.__result
        self.__result = 0
        return result

    def substract(self):
        self.__result = self.numbers[0]
        for number in self.numbers[1:]:
            self.__result -= number
        self.numbers = []
