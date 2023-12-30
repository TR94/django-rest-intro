from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentsDetailSerializer

class CommentList(generics.ListCreateAPIView):
# List takes care of GET method and Create does the POST method
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all() # this line can be used to filter data if required 

    def perform_create(self, serializer):
        # this associates a user with the comment 
        serializer.save(owner=self.request.user)

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    # List takes care of GET, PUT, DELETE methods as used in POST views.py
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentsDetailSerializer
    queryset = Comment.objects.all()
