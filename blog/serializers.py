from rest_framework import serializers
from .models import CreateBlog, Comment
from .forms import BlogForm

class BlogFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogForm
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = CreateBlog
        fields = '__all__'


class CreateBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateBlog
        fields = '__all__'