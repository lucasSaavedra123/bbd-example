from behave import *
from calculator import Calculator

a_calculator = Calculator()

@given('numbers 5, 9, and 10')
def step_impl(context):
    a_calculator.insert(5)
    a_calculator.insert(9)
    a_calculator.insert(10)

@when('the calculator multiplies them')
def step_impl(context):
    a_calculator.multiply()

@then('the result is 450')
def step_impl(context):
    assert a_calculator.result() == 450
