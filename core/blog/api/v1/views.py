from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from .serializers import PostSerializer
from blog.models import Post
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView


'''
class PostList(APIView):
    """show and add posts"""
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    def get(self, request):
        """show all posts"""
        posts = get_list_or_404(Post, status=1)
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
'''

'''
class PostDetail(GenericAPIView):
    """ Show a Single post object plus editing and removing it """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer

    def get(self, request, id):
        """ get post """
        post = get_object_or_404(Post, pk=id, status=1)
        serializer = self.serializer_class(post)
        return Response(serializer.data)

    def put(self, request, id):
        """ update post """
        post = get_object_or_404(Post, pk=id, status=1)
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, id):
        """ delete post """
        post = get_object_or_404(Post, pk=id, status=1)
        post.delete()
        return Response({"detail": "post deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
'''

class PostList(ListCreateAPIView):
    """show and add posts"""
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    queryset = get_list_or_404(Post, status=1)


class PostDetail(RetrieveUpdateDestroyAPIView):
    """ Show a Single post object plus editing and removing it """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=1)