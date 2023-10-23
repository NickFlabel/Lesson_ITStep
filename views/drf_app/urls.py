from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'authors', views.AuthorViewSet)

urlpatterns = [
    path('publishers/', views.get_publishers, name='book_publishers_list'),
    path('publishers/<int:pk>', views.get_publisher, name='book_publisher_detain'),
    path('books/', views.book_list, name='book_book_list'),
    path('books/<int:pk>', views.book_detail, name='book_book_detail')
]

urlpatterns += router.urls
