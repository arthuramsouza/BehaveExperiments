
Feature: Logging in with valid credentials

  Scenario: User logging successfully

    Given I create a new user
    When I type correct email
    When I type correct password
    When I click on 'Login'
    Then I should see the text 'Welcome'