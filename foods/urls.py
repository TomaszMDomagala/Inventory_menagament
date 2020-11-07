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
    path('', PostListView.as_view(), name='index'),
    path('<int:pk>/', PostDetailView.as_view(), name='foods-detail'),
    path('new/', PostCreateView.as_view(), name='foods-create'),
    path('<int:pk>/update', PostUpdateView.as_view(), name='foods-update'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='foods-delete'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
]
