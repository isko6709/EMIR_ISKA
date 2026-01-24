from modeltranslation.translator import TranslationOptions, register
from .models import Region, City, District, Property


@register(Region)
class RegionTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(City)
class CityTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(District)
class DistrictTranslationOptions(TranslationOptions):
    fields = ('name',)


@register(Property)
class PropertyTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'address')
