from django.urls import path
from .views import PostList, PostDetail, CommentsList, CommentsDetail

urlpatterns = [
    # Post paths
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    
    # Comment paths
    path('comments/', CommentsList.as_view(), name='comments-list'),
    path('comments/<int:pk>/', CommentsDetail.as_view(), name='comments-detail'),
]
