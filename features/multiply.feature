Feature: Multiplication
  Calculator should be able to multiply any quantity of numbers

  Scenario: Calculator resolves the multiplication of two numbers
    Given numbers 78 and 5
    When the calculator multiplies these two numbers
    Then the result is 390

  Scenario: Calculator resolves the multiplication of three numbers
    Given numbers 5, 9, and 10
    When the calculator multiplies these three numbers
    Then the result is 450
