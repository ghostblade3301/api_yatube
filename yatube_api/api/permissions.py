from rest_framework.permissions import SAFE_METHODS, BasePermission


# Создаем класс ReadOnlyPermission
class AuthorOrReadOnly(BasePermission):
    # Переопределяем метод has_object_permission,
    # который проверяет, имеет ли пользователь право на чтение объекта
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj.author
