import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from datetime import datetime
from accounts.models import User


@pytest.fixture()
def api_client():
    client = APIClient()
    return client


@pytest.fixture()
def common_user():
    user = User.objects.create_user(email='test@test.ts', password='A@/123456', is_verified = True)
    return user


@pytest.mark.django_db
class TestPostApi:
    def test_get_post_response_200(self, api_client):
        url = reverse('blog:api-v1:post-list')
        response = api_client.get(url)
        assert response.status_code == 200

    def test_create_post_response_401(self, api_client):
        url = reverse('blog:api-v1:post-list')
        data = {
            'status': True,
            'content': 'test',
            'title': 'test',
            'published_date': datetime.now()
        }
        response = api_client.post(url, data=data)
        assert response.status_code == 401

    def test_create_post_response_201(self, api_client, common_user):
        url = reverse('blog:api-v1:post-list')
        data = {
            'status': True,
            'content': 'test',
            'title': 'test',
            'published_date': datetime.now()
        }
        user = common_user
        api_client.force_login(user=user)
        response = api_client.post(url, data=data)
        assert response.status_code == 201

    def test_create_post_bad_data_response_201(self, api_client, common_user):
        url = reverse('blog:api-v1:post-list')
        data = {
            'status': True,
            'content': 'test',
        }
        user = common_user
        api_client.force_login(user=user)
        response = api_client.post(url, data=data)
        assert response.status_code == 400
