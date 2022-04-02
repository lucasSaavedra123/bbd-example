from behave import *
from calculator import Calculator

a_calculator = Calculator()

@given('numbers 5, 1, 10, 0, 20')
def step_impl(context):
    a_calculator.insert(5)
    a_calculator.insert(1)
    a_calculator.insert(10)
    a_calculator.insert(0)
    a_calculator.insert(20)

@when('the calculator sums these five numbers')
def step_impl(context):
    a_calculator.sum()

@then('the result is 36')
def step_impl(context):
    assert a_calculator.result() == 36
