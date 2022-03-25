from behave import *
from calculator import Calculator
from calculator_error import DivisionByZeroError

a_calculator = Calculator()

@given('no numbers')
def step_impl(context):
    pass

@when('we try to divide')
def step_impl(context):
    a_calculator.divide()

@then('the calculator shows error related to no numbers given')
def step_impl(context):
    assert str(a_calculator.result()) == 'No numbers were inserted'
