import json


class TestAPIMainUrl:
    def test_main_api_url_should_response_200(self, client):
        res = client.get('https://ssd-api.jpl.nasa.gov/cad.api')
        assert res.status_code == 200


class TestCheckAPIVersion:
    def test_check_api_version(self, client):
        res = client.get('https://ssd-api.jpl.nasa.gov/cad.api')
        assert res.json().get("signature").get("version") == "1.1"


class TestAPIFields:
    def test_all_fields_are_existed(self, client):
        fields_list = ["des", "orbit_id", "jd", "cd", "dist", "dist_min", "dist_max"]
        res = client.get('https://ssd-api.jpl.nasa.gov/cad.api')
        fields = json.loads(res.text)["fields"]
        # to-do: we should check all fields, not fail the first one
        for field in fields:
            assert field in fields_list


