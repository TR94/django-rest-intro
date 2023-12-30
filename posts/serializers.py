from rest_framework import serializers 
from .models import Post

class PostSerializer(serializers.ModelSerializer):
    # this can be treated like a model form, add extra fields as required
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image =  serializers.ReadOnlyField(source='owner.profile.image.url')

    # built in rest framework validation uses "validate_[field name]"
    def validate_image(self, value):
        if value.size > 1024 * 1024 * 2:
            #2MB file size limit 
            raise serializers.ValidationError(
                'Image size larger than 2MB'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px'
            )
        return value
    
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Post
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'created_at', 'updated_at', 'title', 'content', 'image',
            'image_filter'
        ]

        # note that id has to be added specifically to these fields. 
        # it is already in the models.py file as models.model adds an ID field automatically 
