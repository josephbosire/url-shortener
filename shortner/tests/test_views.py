# -*- coding: utf-8 -*-

from unittest import mock

import pytest
from django.urls import reverse
from django.test import SimpleTestCase


@pytest.mark.vcr(freeze_time="2020-07-27")
@pytest.mark.django_db
def test_shorten_url_success(client):
    url = reverse("shortner:generate-short-url")
    response = client.post(
        path=url, data={"original_url": "https://google.com"},
    )

    expected_response = {
        "status": 200,
        "msg": "OK",
        "data": {
            "original_url": mock.ANY,
            "short_url": mock.ANY,
        },
    }
    assert response.status_code == 200
    assert response.json().items() == expected_response.items()


@pytest.mark.vcr(freeze_time="2020-07-27")
@pytest.mark.django_db
def test_shorten_invalid_url_error(client):
    url = reverse("shortner:generate-short-url")
    response = client.post(
        path=url, data={"original_url": "https://googlem"},
    )

    expected_response = {
        "status": 400,
        "msg": "BAD REQUEST",
        "data": {
            "original_url": [mock.ANY],
        },
    }
    assert response.status_code == 400
    assert response.json().items() == expected_response.items()


@pytest.mark.vcr(freeze_time="2020-07-27")
@pytest.mark.django_db
def test_shorten_url_redirects(client):
    url = reverse("shortner:generate-short-url")
    response = client.post(
        path=url, data={"original_url": "https://google.com"},
    )
    data = response.json()
    short_url = data['data']['short_url']
    response = client.get( path=short_url, follow=False)
    assert response.status_code == 302
    assert response['Location'] == "https://google.com"