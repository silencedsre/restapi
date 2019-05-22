from rest_framework import generics
from .serializers import CommentSerializer
from ..models import Comment

class CommentListAPIView(generics.ListAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        return Comment.objects.all()