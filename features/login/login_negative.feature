
Feature: Attempt to logging in with invalid credentials

  Scenario: None existing user tries to login

    Given I generate a random email address
    When I type random email
    When I type correct password
    When I click on 'Login'
    Then I should see the text 'Error: User not found'

  Scenario: User tries to login with wrong password

    Given I create a new user
    When I type correct email
    When I type random password
    When I click on 'Login'
    Then I should see the text 'Error: Incorrect password'

  Scenario: User tries to login with no password

    Given I create a new user
    When I type correct email
    When I click on 'Login'
    Then I should see the text 'Error: Password field is empty'

  Scenario: User tries to login with invalid email format

    When I type invalid email format
    When I type correct password
    When I click on 'Login'
    Then I should see the text 'Error: Invalid email format'