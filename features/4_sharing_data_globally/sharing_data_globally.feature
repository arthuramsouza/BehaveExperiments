# how to pass data from a step to another

Feature: Sharing data globally

  Scenario: Refund should process
    Given I find recent order from database
    When I issue a refund for the order
    Then the payment gets processed by the user