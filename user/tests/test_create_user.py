import pytest
import json

from datetime import datetime
from rest_framework.test import APIClient

from user.models import User
from user.tests.factories import UserClientFactory


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def data_user_client(faker):
    return {
        "name": faker.name(),
        "last_name": faker.name(),
        "email": faker.email(),
        "password": "12345656",
        "phone_number": faker.msisdn(),
        "user_admin": 0,
    }


URL = "/user/"


@pytest.mark.django_db
def test_if_returns_200(api_client, data_user_client):
    response = api_client.post(
        URL, data=json.dumps(data_user_client), content_type="application/json"
    )
    user = User.objects.last()
    assert response.status_code == 201


@pytest.mark.django_db
def test_fail_if_user_data_already_exist(api_client, data_user_client):
    UserClientFactory()
    data_user_client["email"] = User.objects.last().email
    response = api_client.post(
        URL, data=json.dumps(data_user_client), content_type="application/json"
    )
    assert response.status_code == 400


@pytest.mark.django_db
def test_create_successfully_datas(api_client, data_user_client):
    response = api_client.post(
        URL, data=json.dumps(data_user_client), content_type="application/json"
    )
    user = User.objects.last()
    assert response.status_code == 201
    assert user.name == data_user_client["name"]
    assert user.last_name == data_user_client["last_name"]
    assert user.email == data_user_client["email"]
    assert user.password == data_user_client["password"]
    assert user.phone_number == data_user_client["phone_number"]
