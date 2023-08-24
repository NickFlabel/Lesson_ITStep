from django.urls import path
from .views import get_posts, get_post

# Должна находится переменная-список под названием urlpatterns
# path(<путь к маршруту>, <имя контроллера>: Callable | <вложенный список маршрутов> (include) >
urlpatterns = [
    path('', get_posts),
    # Параметры в url передаются при использовании следующего формата
    # <формат параметра:имя параметра>
    path('posts/<int:post_id>', get_post)
]
