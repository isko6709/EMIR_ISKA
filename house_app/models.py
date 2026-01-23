from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'admin'),
        ('seller', 'seller'),
        ('buyer', 'buyer'),
    )
    age = models.PositiveSmallIntegerField(validators=[MinValueValidator(18),
                                                       MaxValueValidator(99)], default=18)
    email = models.EmailField(unique=True)
    phone_number = PhoneNumberField(null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='buyer')
    preferred_language = models.CharField(max_length=5, default='ru')

    def __str__(self):
        return self.username

class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class City(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class District(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Property(models.Model):
    PROPERTY_TYPE_CHOICES = (
        ('apartment', 'apartment'),
        ('house', 'house'),
        ('land', 'land'),
        ('commercial', 'commercial'),
    )

    CONDITION_CHOICES = (
        ('new', 'new'),
        ('used', 'used'),
        ('needs_repair', 'needs_repair'),
    )

    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    description = models.TextField()

    property_type = models.CharField(max_length=30, choices=PROPERTY_TYPE_CHOICES)

    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True)
    district = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=255)

    area = models.DecimalField(max_digits=8, decimal_places=2)
    price = models.DecimalField(max_digits=12, decimal_places=2)

    rooms = models.PositiveSmallIntegerField(null=True, blank=True)
    floor = models.PositiveSmallIntegerField(null=True, blank=True)
    total_floors = models.PositiveSmallIntegerField(null=True, blank=True)

    condition = models.CharField(max_length=30, choices=CONDITION_CHOICES)

    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/')

class PropertyDocument(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='documents')
    file = models.FileField(upload_to='property_documents/')

class Review(models.Model):
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reviews_written')
    seller = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='reviews_received')
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 6)])
    comment = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.author} -> {self.seller}'
