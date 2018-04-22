from django.urls import path

from .views import PostListView, PostView, NewPostFormView

urlpatterns = [
    path('list', PostListView.as_view(), name='post_list'),
    path('<int:pk>', PostView.as_view(), name='post_detail'),
    path('new', NewPostFormView.as_view(), name='post_new'),
]