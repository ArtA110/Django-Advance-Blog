from django.test import TestCase
from ..models import Post
from datetime import datetime
from accounts.models import User, Profile


class TestModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email="t@test.com", password="/@123456")
        self.profile = Profile.objects.create(
            user=self.user, first_name="test", last_name="test", description="test"
        )

    def test_create_post_with_valid_data(self):
        post = Post.objects.create(
            author=self.profile,
            status=True,
            category=None,
            content="test",
            title="test",
            published_date=datetime.now(),
        )
        self.assertTrue(Post.objects.filter(pk=post.id).exists())
