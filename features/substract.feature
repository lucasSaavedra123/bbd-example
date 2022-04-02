Feature: Substraction
  Calculator should be able to substract any quantity of numbers

  Scenario: Calculator resolves the substraction of two numbers
    Given numbers -57 and 23
    When the calculator resolves -57-23
    Then the result is -80

  Scenario: Calculator resolves the substraction of three numbers
    Given numbers 10, -5, and 20
    When the calculator resolves 10-(-5)-20
    Then the result is -15
