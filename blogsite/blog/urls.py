from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view, 'post_list'),
    path('about/', views.AboutView.as_view(), 'about'),
    path('post/<pk:int>', views.PostDetailView.as_view, 'post_detail'),
    path('post/new/', views.CreatePostView.as_view, name='post_new'),
    path('post/<pk:int>/update/', views.CreateUpdateView.as_view, name='post_update'),
    path('post/<pk:int>/delete/', views.PostDeleteView.as_view, name='post_delete'),
    path('drafts/', views.DraftlistView.as_view, name='post_draft_list')
]