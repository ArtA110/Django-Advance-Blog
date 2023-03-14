from django.urls import path
from blog.api.v1 import views

app_name = 'api-v1'
urlpatterns = [
    path('posts/', views.postList, name='post-list'),
    path('post/<int:id>/', views.postDetail, name='post-detail')
]