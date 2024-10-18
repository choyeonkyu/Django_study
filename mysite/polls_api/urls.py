from django.urls import path, include
from .views import *

urlpatterns = [
    path('questions/', QuestionList.as_view(), name='question-list'),
    path('questions/<int:pk>/', QuestionDetail.as_view(), name='question-detail'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view()),
    path('register/', RegisterUser.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('votes/', VoteList.as_view(), name='vote-list'),
    path('votes/<int:pk>/', VoteDetail.as_view(), name='vote-detail'),
]