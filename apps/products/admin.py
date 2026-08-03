from django.contrib import admin
from django.utils.html import format_html

from .models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "preview",
        "name",
        "price",
        "weight",
        "country",
        "stock",
        "show_on_homepage",
    )

    list_filter = (
        "country",
        "roast_level",
        "show_on_homepage",
    )

    search_fields = (
        "name",
        "description",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }

    list_editable = (
        "price",
        "stock",
        "show_on_homepage",
    )

    def preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" style="border-radius:8px;" />',
                obj.image.url,
            )
        return "-"

    preview.short_description = "Фото"