from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from .serializers import PostSerializer, CategorySerializer
from blog.models import Post, Category
from django.shortcuts import get_object_or_404, get_list_or_404
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import DefaultPagination
from .filters import PostFilter


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


class PostModelViewSet(ModelViewSet):
    """ CRUD for posts """
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=1)
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = PostFilter
    search_fields = ['title', 'content']
    ordering_fields = ['published_date', 'created_date']
    pagination_class = DefaultPagination


class CategoryModelViewSet(ModelViewSet):
    """ CRUD for Category """
    permission_classes = [IsAuthenticated]
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
