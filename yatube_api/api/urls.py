from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from api.views import CommentViewSet, GroupViewSet, PostViewSet


# Создаем роутер и регистрируем необходимые ViewSets
router = DefaultRouter()

# Регистрируем PostViewSet с роутером
router.register('posts', PostViewSet)
# Регистрируем CommentViewSet с роутером
# Параметр post_id используется для получения комментариев к конкретному посту
router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='Comment'
)
# Регистрируем GroupViewSet с роутером
router.register('groups', GroupViewSet)

# Определяем все URL приложения
urlpatterns = [
    # Создаем новый токен для получения учетных данных аутентификации
    path('v1/api-token-auth/', obtain_auth_token),
    # Включаем URL-адреса роутера как единую конечную точку API
    path('v1/', include(router.urls)),
]
