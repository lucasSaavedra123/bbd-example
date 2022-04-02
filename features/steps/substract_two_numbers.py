from behave import *
from calculator import Calculator

a_calculator = Calculator()

@given('numbers -57 and 23')
def step_impl(context):
    a_calculator.insert(-57)
    a_calculator.insert(23)

@when('the calculator resolves -57-23')
def step_impl(context):
    a_calculator.substract()

@then('the result is -80')
def step_impl(context):
    assert a_calculator.result() == -80
