from django.contrib import admin

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "price",
        
    )

    list_filter = (
        "roast_level",
        "weight",
        "country_of_origin",
    )

    search_fields = (
        "name",
    )