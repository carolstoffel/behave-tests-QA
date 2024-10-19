Feature: Random cat facts API
Scenario: Get random cat facts
    When the user requests a random cat fact
    Then the response should contain a random cat fact
