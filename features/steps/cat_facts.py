from behave import given, then, when, step
import requests


@when(u'the user requests a random cat fact')
def step_impl(context):
    context.request = requests.get("https://catfact.ninja/fact")
    assert context.request.status_code == 200    


@then(u'the response should contain a random cat fact')
def step_impl(context):
    assert type(context.request.json()["fact"]) == str
    assert type(context.request.json()["length"]) == int
                
