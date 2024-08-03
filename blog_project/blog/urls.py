# blog/urls.py

from django.urls import path
from .views import RegisterView, LoginView, BlogPostListCreateView, BlogPostDetailView, blog_list_view, blog_detail_view, home_view, contact_view, contact_success

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('posts/', BlogPostListCreateView.as_view(), name='post_list_create'),
    path('posts/<int:pk>/', BlogPostDetailView.as_view(), name='post_detail'),
    path('blog/', blog_list_view, name='blog_list'),
    path('blog/<int:pk>/', blog_detail_view, name='blog_detail'),
    path('home/', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('success/', contact_success, name='contact_success'),
]
