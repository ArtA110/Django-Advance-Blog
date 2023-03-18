from django_filters import rest_framework as filters
from blog.models import Post

class PostFilter(filters.FilterSet):
    """ Custom filter """
    min_published = filters.DateTimeFilter(field_name="published_date", lookup_expr='gte')
    max_published = filters.DateTimeFilter(field_name="published_date", lookup_expr='lte')

    class Meta:
        model = Post
        fields = ['author', 'category']
