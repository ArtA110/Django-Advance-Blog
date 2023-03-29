import pytest
from django.urls import reverse
from rest_framework.test import APIClient
from datetime import datetime


@pytest.mark.django_db
class TestPostApi:
    client = APIClient()
    def test_get_post_response_200(self):
        url = reverse('blog:api-v1:post-list')
        response = self.client.get(url)
        assert response.status_code == 200

    def test_create_post_response_401(self):
        url = reverse('blog:api-v1:post-list')
        data = {
            'status': True,
            'content': 'test',
            'title': 'test',
            'published_date': datetime.now()
        }
        response = self.client.post(url, data=data)
        assert response.status_code == 401
