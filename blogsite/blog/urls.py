from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListView.as_view, 'post_list'),
    path('about/', views.AboutView.as_view(), 'about'),
    path('post/<pk:int>', views.PostDetailView.as_view, 'post_detail'),
    path('post/new/', views.CreatePostView.as_view, name='post_new'),
    path('post/<pk:int>/update/', views.CreateUpdateView.as_view, name='post_update'),
    path('post/<pk:int>/delete/', views.PostDeleteView.as_view, name='post_delete'),
    path('drafts/', views.DraftlistView.as_view, name='post_draft_list'),
    path('post/<pk:int>/comment', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<pk:int>/approve', views.comment_approve, name='comment_approve'),
    path('comment/<pk:int>/remove', views.comment_remove, name='comment_remove'),
    path('post/<pk:int>/publish/', views.post_publish.as_view, name='post_publish'),
]