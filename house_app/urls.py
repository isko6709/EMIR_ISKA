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

router.register(r'users', UserViewSet, basename='users')
router.register(r'regions', RegionViewSet, basename='regions')
router.register(r'cities', CityViewSet, basename='cities')
router.register(r'districts', DistrictViewSet, basename='districts')
router.register(r'properties', PropertyViewSet, basename='properties')
router.register(r'property-images', PropertyImageViewSet, basename='property-images')
router.register(r'property-documents', PropertyDocumentViewSet, basename='property-documents')
router.register(r'reviews', ReviewViewSet, basename='reviews')


urlpatterns = [
    path("", include(router.urls)),
    path('properties-list/', PropertyListAPView.as_view(), name='property-list'),
    path('properties/<int:pk>/', PropertyDetailAPView.as_view(), name='property-detail'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]