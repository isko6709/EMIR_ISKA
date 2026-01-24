from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import (
    UserViewSet,
    RegionViewSet,
    CityViewSet,
    DistrictViewSet,
    PropertyViewSet,
    PropertyImageViewSet,
    PropertyDocumentViewSet,
    ReviewViewSet,
    PropertyListAPIView,
    PropertyDetailAPIView,
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
    path('', include(router.urls)),
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('properties-list/', PropertyListAPIView.as_view(), name='property-list'),
    path('properties/<int:pk>/', PropertyDetailAPIView.as_view(), name='property-detail'),
]
