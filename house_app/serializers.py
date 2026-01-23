from rest_framework import serializers
from .models import (UserProfile, Region, City, District,Property, PropertyImage, PropertyDocument,Review)

from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password', 'first_name', 'last_name',
                  'phone_number', 'age')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = UserProfile.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Неверные учетные данные")

    def to_representation(self, instance):
        refresh = RefreshToken.for_user(instance)
        return {
            'user': {
                'username': instance.username,
                'email': instance.email,
            },
            'access': str(refresh.access_token),
            'refresh': str(refresh),
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('id', 'username', 'email', 'role', 'phone_number', 'preferred_language')


class UserNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username']


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Region
        fields = ['id', 'name']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name']


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'name']


class PropertyImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyImage
        fields = ['image']


class PropertyDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PropertyDocument
        fields = ['file']


class PropertyListSerializer(serializers.ModelSerializer):
    region = RegionSerializer()
    city = CitySerializer()
    district = DistrictSerializer()
    images = PropertyImageSerializer(many=True, read_only=True)

    class Meta:
        model = Property
        fields = [
            'id', 'title', 'price',
            'region', 'city', 'district',
            'images'
        ]


class ReviewSerializer(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format='%d %H:%M')
    author = UserNameSerializer()
    seller = UserNameSerializer()

    class Meta:
        model = Review
        fields = ['id', 'author', 'seller', 'rating', 'comment', 'created_date']


class PropertyDetailSerializer(serializers.ModelSerializer):
    seller = UserNameSerializer()
    region = RegionSerializer()
    city = CitySerializer()
    district = DistrictSerializer()
    images = PropertyImageSerializer(many=True)
    documents = PropertyDocumentSerializer(many=True)
    reviews_written = ReviewSerializer(many=True)

    class Meta:
        model = Property
        fields = [
            'id', 'title', 'description', 'price',
            'region', 'city', 'district', 'address',
            'property_type', 'condition',
            'area', 'rooms', 'floor', 'total_floors',
            'seller',
            'images', 'documents',
            'created_date', 'is_active',
            'reviews_written'
        ]
