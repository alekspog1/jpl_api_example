from pytest_bdd import scenario, given, then, parsers
import datetime

JPL_URL_API = 'https://ssd-api.jpl.nasa.gov/cad.api'


@scenario(
    './query_params.feature',
    'Response with wrong query value should return error and error details'
)
def test_error_details_if_request_wrong_response():
    pass


@given(parsers.parse('As a user I request the wrong body {body}'))
def request_the_body(client, body):
    return client.get(JPL_URL_API, params={'body': body})


@then(parsers.parse('I should see {status_code} error and message: {message}'))
def should_see_the_error_and_error_details(request_the_body, status_code, message):
    assert request_the_body.status_code == 400
    assert request_the_body.json()["message"] == message


@scenario(
    './query_params.feature',
    'We can check PHA objects for the next month'
)
def test_pha_filter():
    pass


@given('As a user I want to request PHA objects for the next two months')
def get_pha_objects(client):
    date_max = (datetime.datetime.now() + datetime.timedelta(days=60)).strftime('%Y-%m-%d')
    return client.get(JPL_URL_API, params={'pha': 'true',
                                           'date-max': date_max
                                           })


@then('I should get list of pha objects')
def check_data_exists(get_pha_objects):
    assert len(get_pha_objects.json()["data"]) > 0
