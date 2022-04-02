from behave import *
from calculator import Calculator

a_calculator = Calculator()

@given('numbers 78 and 5')
def step_impl(context):
    a_calculator.insert(78)
    a_calculator.insert(5)

@when('the calculator multiplies these two numbers')
def step_impl(context):
    a_calculator.multiply()

@then('the result is 390')
def step_impl(context):
    assert a_calculator.result() == 390
