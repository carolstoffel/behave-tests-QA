Feature: Weather 
Scenario: Get weather for Düsseldorf
    Given a weather API
    When requesting weather for 51.233334 latitude and 6.783333 longitude
    Then we should confirm the city as Düsseldorf
    And should receive a response with the current weather data
    And the response should include the temperature, humidity, and weather conditions
