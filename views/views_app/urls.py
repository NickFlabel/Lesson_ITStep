from django.urls import path
from .views import PostById, PostsView

# Должна находится переменная-список под названием urlpatterns
# path(<путь к маршруту>, <имя контроллера>: Callable | <вложенный список маршрутов> (include) >
urlpatterns = [
    path('', PostsView.as_view()),
    # Параметры в url передаются при использовании следующего формата
    # <формат параметра:имя параметра>
    path('posts/<int:post_id>', PostById.as_view())
]
