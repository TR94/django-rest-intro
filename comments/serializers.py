from rest_framework import serializers 
from .models import Comment

class CommentSerializer(serializers.ModelSerializer):
    # this can be treated like a model form, add extra fields as required
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image =  serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'post','profile_id', 'profile_image',
            'created_at', 'updated_at', 'content'
        ]

        # note that id has to be added specifically to these fields. 
        # it is already in the models.py file as models.model adds an ID field automatically 

class CommentsDetailSerializer(CommentSerializer):
    post = serializers.ReadOnlyField(source='post.id')
