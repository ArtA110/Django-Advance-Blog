from django.urls import path
from blog.api.v1 import views

app_name = 'api-v1'
urlpatterns = [
    path('posts/', views.PostList.as_view(), name='post-list'),
    path('post/<int:pk>/', views.PostDetail.as_view(), name='post-detail')
]