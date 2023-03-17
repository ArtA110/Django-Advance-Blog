from django.urls import path
from blog.api.v1 import views
from rest_framework.routers import DefaultRouter

app_name = 'api-v1'

router = DefaultRouter()
router.register('posts', views.PostList, basename='post')

urlpatterns = router.urls

# urlpatterns = [
#     path('posts/', views.PostList.as_view({'get': 'list', 'post': 'create'}), name='post-list'),
#     path('post/<int:pk>/', views.PostList.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='post-detail')
# ]