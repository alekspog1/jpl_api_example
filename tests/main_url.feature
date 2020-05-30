Feature: Main url
    An url with example data.

Scenario: Check that url exist
    Given As a user I request the main page
    Then I should get the "200" status code
    Then I should see some data

Scenario: Check the API version
    Given As a user I request the main page
    Then I should see the API version 1.1

    # It is an example for parametrization tests but honestly it's not good data organization in practice
    # It will be better to make one response, get fields list and compare it with required list
Scenario Outline: Check that all fields are presented
    Given As a user I request the main page
    Then I should see the field: <field>

    Examples:
        | field     |
        | des       |
        | orbit_id  |
        | jd        |
        | cd        |
        | dist      |
        | dist_min  |
        | dist_max  |
        | v_rel     |
        | v_inf     |
        | t_sigma_f |
        | h         |
