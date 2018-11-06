# For demo purposes only
Feature: Demo of displaying output on console
  # Enter feature description here

  Scenario: A test that will pass

    Given I am at the home page
    When I click on 'Contact us'
    Then I should see '123 Testing St.'

  Scenario: A test that will fail

    Given I am at the home page
    When I click on my account
    Then I should see 'Preferences'
