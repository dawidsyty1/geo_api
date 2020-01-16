from django.urls import re_path, path
from accounts import views
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('obtain_token', obtain_jwt_token, name='api-jwt-auth'),
    path('create_user', views.UserCreateView.as_view({'post': 'create'}), name='user-create'),
]
