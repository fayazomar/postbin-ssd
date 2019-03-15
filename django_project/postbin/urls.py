from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='postbin-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/results', PostListView.as_view(), name='search'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/private_posts', PostListView.as_view(template_name='postbin/private_posts.html'), name='post-private'),
    path('post/invite_posts', PostListView.as_view(template_name='postbin/invite_posts.html'), name='post-invite'),
    path('about/', views.about, name='postbin-about'),
]
