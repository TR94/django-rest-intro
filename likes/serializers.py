from django.db import IntegrityError
from rest_framework import serializers 
from .models import Likes

class LikeSerializer(serializers.ModelSerializer):
    # this can be treated like a model form, add extra fields as required
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Likes
        fields = [
            'id','owner','created_at','post'   
        ]

    # to handle a user liking the same post twice 
    def create(self, validated_data):
        try: 
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail':'possible duplicate'
            })