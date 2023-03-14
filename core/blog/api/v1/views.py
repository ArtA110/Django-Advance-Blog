from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from blog.models import Post
from django.shortcuts import get_object_or_404, get_list_or_404

@api_view()
def postList(request):
    posts = get_list_or_404(Post, status=1)
    posts = PostSerializer(posts, many=True)
    return Response(posts.data)

@api_view()
def postDetail(request, id):
    post = get_object_or_404(Post, pk=id, status=1)
    post = PostSerializer(post)
    return Response(post.data)
