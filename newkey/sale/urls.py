from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostDeleteView

urlpatterns = [
    path('', PostListView.as_view(), name='PostListView'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='PostDetailView'),
    path('post/new/', PostCreateView.as_view(), name='PostCreateView'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='PostDeleteView')
]
