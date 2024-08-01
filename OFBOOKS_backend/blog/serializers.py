from rest_framework import serializers

from account.serializers import UserSerializer
from account.models import User
from .models import Paragraph, Blog, Tag, Like

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = (
            'id',
            'name',
            'is_trend'
        ) 


class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = (
            'id',
            'title',
            'body',
        ) 


class BlogSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    tags = TagSerializer(read_only=True, many=True)
    is_liked = serializers.SerializerMethodField()
    class Meta:
        model = Blog
        fields = (
            'id',
            'title',
            'description',
            'created_by',
            'created_at_formatted',
            'get_image',
            'tags',
            'like_count',
            'is_liked',
        )

    def get_is_liked(self, obj):
        try:
            user = User.objects.get(pk=self.context.get("user_id"))
            like = Like.objects.get(created_by=user, created_for=obj)
        except:
            return False
        return True


class BlogDetailSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    paragraphs = ParagraphSerializer(read_only=True, many=True)
    tags = TagSerializer(read_only=True, many=True)
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = (
            'id',
            'title',
            'description',
            'created_by',
            'created_at_formatted',
            'get_image',
            'paragraphs',
            'tags',
            'like_count',
            'is_liked',
        )

    def get_is_liked(self, obj):
        try:
            user = User.objects.get(pk=self.context.get("user_id"))
            like = Like.objects.get(created_by=user, created_for=obj)
        except:
            return False
        return True