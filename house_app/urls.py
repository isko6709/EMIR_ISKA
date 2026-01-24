from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import (
    UserViewSet,
    RegionViewSet,
    CityViewSet,
    DistrictViewSet,
    PropertyListAPView,
    PropertyDetailAPView,
    PropertyViewSet,
    PropertyImageViewSet,
    PropertyDocumentViewSet,
    ReviewListAPView,
    ReviewViewSet,
    RegisterView,
    LoginView,
    LogoutView,
)

router = SimpleRouter()

urlpatterns = [
    path("", include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]