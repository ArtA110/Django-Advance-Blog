from django.urls import path
from blog import views

app_name = 'blog'
urlpatterns = [
    path('redirect/<int:pk>',views.RedirectToGoogle.as_view(),name='redirect-to-google'),
    path('posts/',views.PostListView.as_view(),name='post-list'),
    path('posts/<int:pk>/', views.PostDetailView.as_view(),name='post-detail')
]