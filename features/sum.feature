Feature: Sum
  Calculator should be able to sums any quantity of numbers

  Scenario: Calculator resolves the sum of two numbers
    Given numbers 10 and 97
    When the calculator sums these two numbers
    Then the result is 107
  
  Scenario: Calculator resolves the sum of five numbers
    Given numbers 5, 1, 10, 0, 20
    When the calculator sums these five numbers
    Then the result is 36
