from rest_framework import serializers
from blog.models import Post, Category


class PostSerializer(serializers.ModelSerializer):
    snippet = serializers.ReadOnlyField(source='get_snippet')
    relative_url = serializers.URLField(source='get_absolute_api_url', read_only=True)
    absolute_url = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = ['id', 'title', 'status', 'content', 'snippet', 'author', 'absolute_url', 'relative_url',
                  'created_date', 'published_date']
    def get_absolute_url(self, obj):
            request = self.context.get('request')
            return request.build_absolute_uri(obj.pk)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
