from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.get_authors, name='book_authors_list'),
    path('authors/<int:pk>', views.get_author, name='book_author_detain'),
    path('publishers/', views.get_publishers, name='book_publishers_list'),
    path('publishers/<int:pk>', views.get_publisher, name='book_publisher_detain'),
    path('books/', views.book_list, name='book_book_list'),
    path('books/<int:pk>', views.book_detail, name='book_book_detail')
]
