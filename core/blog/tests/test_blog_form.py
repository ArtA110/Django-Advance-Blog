from django.test import TestCase
from ..forms import PostForm
from datetime import datetime
from ..models import Category


class TestPostForm(TestCase):

    def test_postform_with_valid_data(self):
        category = Category.objects.create(name='test')
        form = PostForm(data={
            'title': 'test',
            'content': 'test',
            'status': True,
            'published_date': datetime.now(),
            'category': category
        })
        self.assertTrue(form.is_valid())

    def test_postform_with_no_data(self):
        form = PostForm(data={})
        self.assertFalse(form.is_valid())
