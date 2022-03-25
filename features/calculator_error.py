class CalculatorError():
    def thereIsError(self):
        return True

class EmptyError(CalculatorError):
    def thereIsError(self):
        return False

    def __str__(self):
        return 'No Error'

class DivisionByZeroError(CalculatorError):
    def __str__(self):
        return 'Zero division is not allowed'

class NoNumbersInsertedError(CalculatorError):
    def __str__(self):
        return 'No numbers were inserted'
