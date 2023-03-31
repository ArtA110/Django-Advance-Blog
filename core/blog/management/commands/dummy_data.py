import random
from django.core.management.base import BaseCommand
from accounts.models import User, Profile
from blog.models import Post, Category
from faker import Faker
from datetime import datetime

category_list = ['Technology', 'Python', 'Fun', 'Django']


class Command(BaseCommand):
    help = 'Add dummy data to DB'

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.faker = Faker()

    def handle(self, *args, **options):
        user = User.objects.create_user(
            email=self.faker.email(),
            password='A@/123456',
            is_verified=True
        )
        profile = Profile.objects.get(user=user)
        (profile.first_name, profile.last_name) = self.faker.name().split(' ')
        profile.description = self.faker.paragraph(nb_sentences=5)
        profile.save()

        for name in category_list:
            Category.objects.get_or_create(name=name)

        for _ in range(10):
            Post.objects.create(
                author=profile,
                published_date=datetime.now(),
                title=self.faker.paragraph(nb_sentences=1),
                content=self.faker.paragraph(nb_sentences=10),
                status=random.choice([True, False]),
                category=Category.objects.get(name=random.choice(category_list))
            )
