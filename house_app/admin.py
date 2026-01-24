from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import (
    UserProfile,
    Region,
    City,
    District,
    Property,
    PropertyImage,
    PropertyDocument,
    Review,
)
class TranslationMedia(TranslationAdmin):
    class Media:
        js = (
            'https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js',
            'https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1

    def __str__(self):
        return f'Image for {self.property.title}'


class PropertyDocumentInline(admin.TabularInline):
    model = PropertyDocument
    extra = 1

    def __str__(self):
        return f'Image for {self.property.title}'


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'region')
    list_filter = ('region',)
    search_fields = ('name',)


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city')
    list_filter = ('city',)
    search_fields = ('name',)

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImageInline, PropertyDocumentInline]

    list_display = (
        'id',
        'title',
        'price',
        'area',
        'rooms',
        'property_type',
        'condition',
        'city',
        'seller',
        'is_active',
        'created_date',
    )

    list_filter = (
        'property_type',
        'condition',
        'region',
        'city',
        'is_active',
    )

    search_fields = (
        'title',
        'description',
        'address',
    )

    autocomplete_fields = ('seller', 'region', 'city', 'district')

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'username',
        'email',
        'role',
        'age',
        'preferred_language',
        'is_active',
        'is_staff',
    )

    list_filter = ('role', 'preferred_language', 'is_active')
    search_fields = ('username', 'email')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'author',
        'seller',
        'rating',
        'created_date',
    )

    list_filter = ('rating',)
    search_fields = ('comment',)
