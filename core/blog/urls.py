from django.urls import path
from blog import views

app_name = 'blog'
urlpatterns = [
    path('redirect/<int:pk>',views.RedirectToGoogle.as_view(),name='redirect-to-google'),
    path('posts/',views.PostListView.as_view(),name='post-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(),name='post-detail'),
    path('posts/new/', views.PostCreateView.as_view(),name = 'post-create'),
    path('posts/<int:pk>/edit/', views.PostEditView.as_view(), name= 'edit-view'),
    path('posts/<int:pk>/delete/', views.PostDeleteView.as_view(), name= 'delete-view'),
    # REST
    path('post/', views.api_post_list_view, name='API-post-list')
]