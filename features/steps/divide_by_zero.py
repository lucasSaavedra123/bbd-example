from behave import *
from calculator import Calculator
from calculator_error import DivisionByZeroError

a_calculator = Calculator()

@given('numbers 4 and 0')
def step_impl(context):
    a_calculator.insert(4)
    a_calculator.insert(0)

@when('the calculator divides them')
def step_impl(context):
    a_calculator.divide()

@then('the calculator fails to show result')
def step_impl(context):
    assert str(a_calculator.result()) == 'Zero division is not allowed'
