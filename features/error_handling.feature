Feature: Error Handling
  Calculator shows errors

  Scenario: no numbers are given
    Given no numbers
    When we try to divide
    Then the calculator shows error related to no numbers given

  Scenario: calculator tries to divide 4 by 0
    Given numbers 4 and 0
    When the calculator divides them
    Then the calculator fails to show result
