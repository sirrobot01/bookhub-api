from django.contrib import admin
from django.urls import include, path
from rest_framework_jwt.views import refresh_jwt_token, verify_jwt_token
from .doc import urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_auth.urls')),
    path('auth/register/', include('rest_auth.registration.urls')),
    path('auth/refresh/', refresh_jwt_token, name='refresh-token'),
    path('auth/verify/', verify_jwt_token, name='verify-token'),
    path('users/', include('users.urls')),
    path('api/v1/', include('api.urls'))
] + urls
