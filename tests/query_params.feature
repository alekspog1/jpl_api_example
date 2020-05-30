Feature: Query Params
  Params should work

Scenario: Response with wrong query value should return error and error details
    Given As a user I request the wrong body "sun"
    Then I should see "400" error and message: body not found

Scenario: We can check PHA objects for the next two months
  Given As a user I want to request PHA objects for the next two months
  Then I should get list of pha objects
