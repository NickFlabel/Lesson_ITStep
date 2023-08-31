from django.urls import path
from .views import CreateAutorView, AuthorList, AuthorDetail, UpdateAuthorView, DeleteAuthorView

urlpatterns = [
    path('authors/', AuthorList.as_view(), name='author_list'),
    path('authors/create/', CreateAutorView.as_view(), name='author_create'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='author_detail'),
    path('authors/<int:pk>/update/', UpdateAuthorView.as_view(), name='author_update'),
    path('authors/<int:pk>/delete/', DeleteAuthorView.as_view(), name='author_delete')
]
