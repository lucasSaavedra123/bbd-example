from behave import *
from calculator import Calculator

a_calculator = Calculator()

@given('numbers 100, -5, and -1')
def step_impl(context):
    a_calculator.insert(100)
    a_calculator.insert(-5)
    a_calculator.insert(-1)

@when('the calculator resolve (100/-5)/-1')
def step_impl(context):
    a_calculator.divide()

@then('the result is 20')
def step_impl(context):
    result = a_calculator.result()
    assert result == 20, result
