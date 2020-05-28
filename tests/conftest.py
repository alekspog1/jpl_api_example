import pytest
import requests


@pytest.fixture(scope="session")
def client():
    return requests.Session()
