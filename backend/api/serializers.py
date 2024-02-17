from rest_framework import serializers
from .models import Forum, News, NewsComments, User

class ForumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Forum
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class NewsCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsComments
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'