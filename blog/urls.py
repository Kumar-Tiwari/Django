from django.urls import path
from .views import AboutView,PostListView,PostDetailView,CreatePostView,PostUpdateView,PostDeleteView,DraftListView,add_comment_to_post,comment_approved,comment_removed,post_publish
urlpatterns=[
    path('',PostListView.as_view(),name='post_list'),
    path('about/',AboutView.as_view(),name='about'),
    path('post/<int:pk>',PostDetailView.as_view(),name='post_detail'),

    path('post/new',CreatePostView.as_view(),name='post_new'),
    path('post/<int:pk>',PostUpdateView.as_view(),name='post_edit'),
    path('post/<int:pk>/remove',PostDeleteView.as_view(),name='post_remove'),
    path('drafts/',DraftListView.as_view(),name='post_draft_list'),
    path('post<int:pk>/comments',add_comment_to_post,name='add_comment_to_post'),
    path('comment/<int:pk>/approved/',comment_approved,name='comment_approved'),
    path('comment/<int:pk>/remove',comment_removed,name='comment_removed'),
    path('post/<int:pk>/publish',post_publish,name='post_publish'),
]