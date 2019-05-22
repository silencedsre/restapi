from django.urls import path, include
from .views import CommentListAPIView
app_name = 'comments'
urlpatterns = [
    path('', CommentListAPIView.as_view(), name='list' ) #api/commentp
]