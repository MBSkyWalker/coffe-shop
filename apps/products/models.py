from django.shortcuts import render
from django.db import models

class RoastLevel(models.TextChoices):

    LIGHT = "light", "Light"
    MEDIUM = "medium", "Medium"
    DARK = "dark", "Dark"


class WeightChoices(models.IntegerChoices):
    G250 = 250, "250g"
    G500 = 500, "500g"
    G1000 = 1000, "1kg"


class Product(models.Model):

    # Основна інформація про продукт
    name = models.CharField(
        "Назва",
        max_length=200
)

    brand = models.CharField(
        "Бренд",
        max_length=100,
        default="Unknown"
    )

    description = models.TextField(
        "Опис"
)

    brief_description = models.CharField(
        "Короткий опис", max_length=200, blank=True)

    slug = models.SlugField(
    unique=True,
    verbose_name="Slug",
    blank=True,
)

    # Комерційна інформація про продукт
    price = models.DecimalField(
        "Ціна",
         max_digits=8,
          decimal_places=2
)

    stock = models.PositiveIntegerField(
        "Кількість на складі",
        default=0
    )
    
    # Характеристики продукту
    weight = models.PositiveIntegerField(
        choices=WeightChoices.choices,
        default=WeightChoices.G1000,
    )

    country = models.CharField(
        "Країна виробник",
        max_length=100,
        default="Unknown"
    )

    roast_level = models.CharField(
    max_length=20,
    choices=RoastLevel.choices,
    default=RoastLevel.MEDIUM,
)

    # Відображення 
    show_on_homepage = models.BooleanField(default=False, verbose_name=
        "Показувати на головній сторінці",
)

    image = models.ImageField(
        "Зображення",
        upload_to="products/"
    )


    
    #Службова інформація
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    is_featured = models.BooleanField(
        default=False,
        verbose_name="Рекомендований продукт"
    )

    is_new = models.BooleanField(
        default=False,
        verbose_name="Новий продукт"
    )

    

    

    def get_absolute_url(self):
        from django.urls import reverse

        return reverse(
            "product_detail",
            kwargs={
                "slug": self.slug
            },
        )

    class Meta:
        ordering = ["-created_at"]
        verbose_name = "Товар"
        verbose_name_plural = "Товары"

    @property
    def is_available(self):
        return self.stock > 0

    def __str__(self):
        return f'{self.name} ({self.weight}) г '

        

