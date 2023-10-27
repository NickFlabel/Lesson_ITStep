from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

schema_view = get_schema_view(
    openapi.Info(
        title='ITStep DB API',
        default_version='v1',
        description='Test',
        terms_of_service='',
        contact=openapi.Contact(email=''),
        license=openapi.License(name='')
    ),
    public=True
)

router = DefaultRouter()
router.register('authors', views.AuthorViewSet)
router.register('books', views.BookViewSet, basename='books')
router.register('locations', views.LocationViewSet)

urlpatterns = [
    path('publishers/', views.get_publishers, name='book_publishers_list'),
    path('publishers/<int:pk>', views.get_publisher, name='book_publisher_detain'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger_ui'),
    path('token/', TokenObtainPairView.as_view(), name='api_login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='api_refresh'),
    path('create_user/', views.CreateUserView.as_view()),
    path('auth/', views.authenticate_user)
]

urlpatterns += router.urls
