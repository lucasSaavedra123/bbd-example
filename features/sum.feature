Feature: Sum
  We use a calculator that sums any quantity of numbers

  Scenario: sum
    Given numbers 10 and 97
    When the calculator sums them
    Then the result is 107