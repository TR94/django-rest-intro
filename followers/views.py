from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowSerializer


class FollowerList(generics.ListCreateAPIView):
# List takes care of GET method and Create does the POST method
    serializer_class = FollowSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all() # this line can be used to filter data if required 

    def perform_create(self, serializer):
        # this associates a user with the follow
        serializer.save(owner=self.request.user)

class FollowerDetail(generics.RetrieveDestroyAPIView):
    # List takes care of GET, DELETE methods as used in POST views.py
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FollowSerializer
    queryset = Follower.objects.all()