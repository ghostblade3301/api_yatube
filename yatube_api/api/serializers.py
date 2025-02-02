from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Group, Post


# Сериализатор для модели Post
class PostSerializer(serializers.ModelSerializer):

    # Установить поле автора только для чтения
    author = SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    # Мета-класс определяет модель и поля для сериализации
    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image', 'group', 'pub_date')


# Сериализатор для модели Group
class GroupSerializer(serializers.ModelSerializer):

    # Мета-класс определяет модель и поля для сериализации
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


# Сериализатор для модели Comment
class CommentSerializer(serializers.ModelSerializer):

    # Установить поля автора и поста только для чтения
    author = SlugRelatedField(
        slug_field='username',
        read_only=True,
    )

    # Мета-класс определяет модель и поля для сериализации
    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
        read_only_fields = ('post',)
