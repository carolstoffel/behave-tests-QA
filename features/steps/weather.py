from behave import given, when, then
import requests
from util.util import get_city_by_lat_and_long
import os 


WEATHER_API_KEY = os.environ.get("WEATHER_API_KEY")

@given(u'a weather API')
def step_impl(context):
    context.url = "https://api.openweathermap.org/data/3.0/onecall"


@when(u'requesting weather for {latitude} latitude and {longitude} longitude')
def step_impl(context, latitude, longitude):
    context.latitude = latitude
    context.longitude = longitude
    context.city = get_city_by_lat_and_long(latitude,longitude)


@then(u'we should confirm the city as {city}')
def step_impl(context, city):
    assert context.city == city
    
    
@then(u'should receive a response with the current weather data')
def step_impl(context):
    context.response_api = requests.get(f"{context.url}?lat={context.latitude}&lon={context.longitude}&appid={WEATHER_API_KEY}")
    assert context.response_api.status_code == 200


@then(u'the response should include the temperature, humidity, and weather conditions')
def step_impl(context):
    assert "current" in context.response_api.json()
    required = ["temp", "humidity", "clouds"]
    for attr in required:
        assert attr in context.response_api.json()["current"]
    