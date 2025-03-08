import pytest
import json
from datetime import datetime
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def data_user_client():
    return {
        "name": "nometeste",
        "last_name": "sobrenome",
        "email": "emailtest@gmail.com",
        "password": "12345656",
        "phone_number": "999999999",
        "user_admin": 0,
        "created_at": "2025-12-02",
    }


URL = "/user/"


@pytest.mark.django_db
def test_if_returns_200(api_client, data_user_client):
    breakpoint()
    response = api_client.post(
        URL, data=json.dumps(data_user_client), content_type="application/json"
    )
    assert response.status_code == 201
