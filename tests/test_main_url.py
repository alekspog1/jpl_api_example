from pytest_bdd import scenario, given, then, parsers

JPL_URL_API = 'https://ssd-api.jpl.nasa.gov/cad.api'


@scenario("./main_url.feature", "Check that url exist")
def test_main_url_exist():
    pass


@given("As a user I request the main page")
def request_the_main_page(client):
    return client.get(JPL_URL_API)


@then(parsers.parse('I should get the "{code:d}" status code'))
def check_status_code(request_the_main_page, code):
    assert request_the_main_page.status_code == code


@then("I should see some data")
def check_data_exist(request_the_main_page):
    assert len(request_the_main_page.json()["data"]) > 0


@scenario("./main_url.feature", "Check the API version")
def test_api_version():
    pass


@given("As a user I request the main page")
def request_the_main_page(client):
    return client.get(JPL_URL_API)


@then(parsers.parse('I should see the API version {version}'))
def check_api_version(request_the_main_page, version):
    assert request_the_main_page.json()["signature"]["version"] == version


@then("I should see some data")
def check_that_data_exist(request_the_main_page):
    assert len(request_the_main_page.json()["data"]) > 0


@scenario(
    './main_url.feature',
    'Check that specific field is presented',
    example_converters=dict(field=str)
)
def test_check_the_field():
    pass


@then("I should see the field: <field>")
def check_field(request_the_main_page, field):
    assert field in request_the_main_page.json()["fields"]
