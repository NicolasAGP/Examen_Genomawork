from django.contrib import admin
from .models import restaurant, Restauran_ubicacion


@admin.register(restaurant)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'Restauran_ubicacion', 'active']
    list_filter = ['active', 'Restauran_ubicacion', ]
    readonly_fields = ['tag_category', ]
    search_fields = ['name', 'category__title']


@admin.register(Restauran_ubicacion)
class CategoryAdmin(admin.ModelAdmin):
    list_filter = ['active',]
    list_display = ['id', 'title', 'active']
