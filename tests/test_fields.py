from pytest_bdd import scenario, given, then, parsers

JPL_URL_API = 'https://ssd-api.jpl.nasa.gov/cad.api'


@scenario("main_url.feature", "Check that url exist")
def test_main_url_exist():
    pass


@given("As a user I request the main page")
def request_the_main_page(client):
    return client.get(JPL_URL_API)


@then("I should get the 200 status code")
def check_status_code(request_the_main_page):
    assert request_the_main_page.status_code == 200


@then("I should see some data")
def check_data_exist(request_the_main_page):
    assert len(request_the_main_page.json()["data"]) > 0


@scenario("main_url.feature", "Check the API version")
def test_api_version():
    pass


@then(parsers.parse('I should see the API version {version}'))
def check_status_code(request_the_main_page, version):
    assert request_the_main_page.json()["signature"]["version"] == version


@then("I should see some data")
def check_data_exist(request_the_main_page):
    assert len(request_the_main_page.json()["data"]) > 0
