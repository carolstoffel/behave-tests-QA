# behave-tests-QA

This repository allows users to test the retrieval of current weather information for a specified location using a weather API ([OpenWeatherMap](https://api.openweathermap.org)). Note that an account is required to access the API.

Additionally, it includes a basic test for retrieving cat facts from the Cat Facts API ([catfact.ninja](https://catfact.ninja/fact)).

## Create Virtual Environment

To create a new environment, run:

```bash
python3 -m venv behave-tests
```

Activate the environment:
```bash
source behave-tests/bin/activate
```

Deactivate the environment:
```bash
deactivate
```

## Prerequisites
To install the prerequisites, run:
```bash
python install -r requirements.txt
```


## Execution
```bash
behave features/cat_facts
behave features/weather
```