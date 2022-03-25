Feature: Substraction
  We use a calculator that substract all the number passed

  Scenario: calculator resolves 90-100-10
    Given numbers 90, 100, and 10
    When the calculator resolves 90-100-10
    Then the result is -20
