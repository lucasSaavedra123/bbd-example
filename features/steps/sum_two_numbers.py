from behave import *
from calculator import Calculator

a_calculator = Calculator()

@given('numbers 10 and 97')
def step_impl(context):
    a_calculator.insert(10)
    a_calculator.insert(97)

@when('the calculator sums these two numbers')
def step_impl(context):
    a_calculator.sum()

@then('the result is 107')
def step_impl(context):
    assert a_calculator.result() == 107
