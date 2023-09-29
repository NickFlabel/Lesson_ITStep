from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.get_authors, name='book_authors_list'),
    path('authors/<int:pk>', views.get_author, name='book_author_detain'),
    path('publishers/', views.get_publishers, name='book_publishers_list')
]
