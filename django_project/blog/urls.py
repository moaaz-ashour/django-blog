from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreatelView
)
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new', PostCreatelView.as_view(), name='post-create'),
    path('about/', views.about, name='blog-about'),
]
