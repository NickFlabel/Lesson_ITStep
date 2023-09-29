from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', include('views_app.urls')),
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('accounts/', include('accounts.urls')),
    path('api/', include('drf_app.urls'))
]
