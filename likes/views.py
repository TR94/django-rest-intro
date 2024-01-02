from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from likes.models import Likes
from likes.serializers import LikeSerializer


class LikeList(generics.ListCreateAPIView):
# List takes care of GET method and Create does the POST method
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Likes.objects.all() # this line can be used to filter data if required 

    def perform_create(self, serializer):
        # this associates a user with the like
        serializer.save(owner=self.request.user)

class LikeDetail(generics.RetrieveDestroyAPIView):
    # List takes care of GET, DELETE methods as used in POST views.py
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Likes.objects.all()