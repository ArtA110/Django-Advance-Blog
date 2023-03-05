from django.urls import path
from blog import views

urlpatterns = [
    path('redirect/<int:pk>',views.RedirectToGoogle.as_view(),name='redirect-to-google'),
    path('posts',views.PostList.as_view(),name='post-list')
]