from django.shortcuts import render
from django.db import models

class Product(models.Model):
    name = models.CharField("Назва", max_length=200)
    description = models.TextField("Опис")
    price = models.DecimalField("Ціна", max_digits=8, decimal_places=2)

    image = models.ImageField(
        "Зображення",
        upload_to="products/"
    )

    is_available = models.BooleanField(
        "Наявність",
        default=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        ordering = ["name"]
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    def __str__(self):
        return self.name

