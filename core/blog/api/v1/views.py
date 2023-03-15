from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PostSerializer
from blog.models import Post
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status


@api_view(['GET', 'POST'])
def postList(request):
    if request.method == 'GET':
        posts = get_list_or_404(Post, status=1)
        posts = PostSerializer(posts, many=True)
        return Response(posts.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def postDetail(request, id):
    post = get_object_or_404(Post, pk=id, status=1)
    if request.method == 'GET':
        post = PostSerializer(post)
        return Response(post.data)
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        post.delete()
        return Response({"detail": "post deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
