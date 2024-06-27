from django.urls import path
from . views import ListCustomUsersApiView, CreateCustomUserApiView, ListItemApiView, DetailItemApiView, QRCodeApiView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('register', CreateCustomUserApiView.as_view(), name='signup'),
    path('login', TokenObtainPairView.as_view(), name='signin'),
    path('refresh', TokenRefreshView.as_view(), name='refresh'),
    path('users', ListCustomUsersApiView.as_view(), name='list-users'),
    path('items', ListItemApiView.as_view(), name='list-items'),
    path('items/<int:id>', DetailItemApiView.as_view(), name='detail-item'),
    path('qrcode', QRCodeApiView.as_view(), name='qrcode'),
]