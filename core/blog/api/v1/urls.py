from django.urls import path
from blog.api.v1 import views
from rest_framework.routers import DefaultRouter

app_name = "api-v1"

router = DefaultRouter()
router.register("post", views.PostModelViewSet, basename="post")
router.register("category", views.CategoryModelViewSet, basename="category")

urlpatterns = router.urls

# urlpatterns = [
#     path('posts/', views.PostList.as_view({'get': 'list', 'post': 'create'}), name='post-list'),
#     path('post/<int:pk>/', views.PostList.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='post-detail')
# ]
