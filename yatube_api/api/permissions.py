from rest_framework.permissions import SAFE_METHODS, BasePermission


# Создаем класс ReadOnlyPermission
class ReadOnlyPermission(BasePermission):
    # Переопределяем метод has_object_permission,
    # который проверяет, имеет ли пользователь право на чтение объекта
    def has_object_permission(self, request, view, obj):
        # Если метод запроса находится в списке SAFE_METHODS
        # если они совпадают, то возвращаем True, разрешая соединение,
        # в противном случае возвращаем False, запрещая соединение
        if request.method in SAFE_METHODS:
            return True
        return request.user == obj.author
