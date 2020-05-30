Feature: Main url
    An url with example data.

Scenario: Check that url exist
    Given As a user I request the main page
    Then I should get the "200" status code
    Then I should see some data

Scenario: Check the API version
    Given As a user I request the main page
    Then I should see the API version 1.1

