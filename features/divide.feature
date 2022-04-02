Feature: Division
  Calculator should be able to divide any quantity of numbers

  Scenario: divide numbers 70 and 4
    Given numbers 70 and 4
    When the calculator resolve 70 divided by 4
    Then the result is 17.5

  Scenario: divide numbers 100, -5, -1
    Given numbers 100, -5, -1
    When the calculator resolve (100/-5)/-1
    Then the result is 20
