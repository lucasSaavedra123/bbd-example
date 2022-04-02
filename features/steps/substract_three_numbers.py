from behave import *
from calculator import Calculator

a_calculator = Calculator()

@given('numbers 10, -5, and 20')
def step_impl(context):
    a_calculator.insert(90)
    a_calculator.insert(100)
    a_calculator.insert(10)

@when('the calculator resolves 10-(-5)-20')
def step_impl(context):
    a_calculator.substract()

@then('the result is -15')
def step_impl(context):
    assert a_calculator.result() == -20
