from django.test import TestCase, Client
from django.urls import reverse
from ..models import Post
from datetime import datetime
from accounts.models import User, Profile


class TestView(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(email="t@test.com", password="/@123456")
        self.profile = Profile.objects.create(
            user=self.user, first_name="test", last_name="test", description="test"
        )
        self.post = Post.objects.create(
            author=self.profile,
            status=True,
            category=None,
            content="test",
            title="test",
            published_date=datetime.now(),
        )

    def test_blog_postlist_successful_response(self):
        url = reverse("blog:post-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(str(response.content).find("All published posts"))
        self.assertTemplateUsed(response, template_name="blog/post_list.html")

    def test_blog_postdetail_logged_in_response(self):
        self.client.force_login(user=self.user)
        url = reverse("blog:post-detail", kwargs={"pk": self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_blog_postdetail_anonymous_response(self):
        url = reverse("blog:post-detail", kwargs={"pk": self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)
