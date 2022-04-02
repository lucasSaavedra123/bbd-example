Feature: Error Handling
  Users make mistakes. And sometimes they don't know
  what It does mean 'indefined'. Thus, we have to
  guide them to the correct input. Calculator should
  be able to report user about errors.

  Scenario: Calculator fails when result tries an operation and no numbers were given
    Given no numbers
    When we try to divide
    Then the calculator shows error related to no numbers given

  Scenario: Calculator fails when result tries a division with zero
    Given numbers 4 and 0
    When the calculator divides them
    Then the calculator fails to show result
