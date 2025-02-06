from django.contrib import admin
from .models import CarMake, CarModel


# CarModelInline class
class CarModelInline(admin.TabularInline):
    model = CarModel
    extra = 1  # Número de formularios adicionales para añadir nuevos modelos


# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'car_make', 'type', 'year', 'horsepower',
                    'color', 'price', 'transmission')
    search_fields = ('name', 'car_make__name')
    list_filter = ('type', 'year', 'color')


# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
    inlines = [CarModelInline]
    list_display = ('name', 'description',
                    'country', 'founded_year', 'website')
    search_fields = ('name', 'country')


# Register models here
admin.site.register(CarMake, CarMakeAdmin)
admin.site.register(CarModel, CarModelAdmin)