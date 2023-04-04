from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from posts.models import Group, Post
from .permissions import AuthorOrReadOnly
from .serializers import CommentSerializer, GroupSerializer, PostSerializer


# Post ViewSet
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated & AuthorOrReadOnly]

    # Переопределение perform_create для связывания автора с постом
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


# Group ViewSet
class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]


# Comment ViewSet
class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated & AuthorOrReadOnly]

    # Переопределение get_queryset для возвращения комментов к опр. посту
    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)
        return post.comments.all()

    # Переопределение perform_create для связки автора и поста с комментарием
    def perform_create(self, serializer):
        serializer.save(
            author=self.request.user,
            post_id=self.kwargs.get('post_id')
        )
