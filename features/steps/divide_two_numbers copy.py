from behave import *
from calculator import Calculator

a_calculator = Calculator()

@given('numbers 70 and 4')
def step_impl(context):
    a_calculator.insert(70)
    a_calculator.insert(4)

@when('the calculator resolve 70 divided by 4')
def step_impl(context):
    a_calculator.divide()

@then('the result is 17.5')
def step_impl(context):
    assert a_calculator.result() == 17.5
