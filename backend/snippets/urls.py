from django.urls import path
from snippets import views

urlpatterns = [
  path('', views.api_root),
  path('snippets', views.SnippetList.as_view(), name='snippet-list'),
  path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
  path('snippets/<int:pk>/highlight/', views.SnippetHighlight.as_view()),
  path('users/', views.UserList.as_view(), name='user-list'),
  path('users/<int:pk>/', views.UserDetail.as_view()),
]