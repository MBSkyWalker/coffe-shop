from django.shortcuts import render

from apps.products.models import Product


def home(request):

    products = Product.objects.filter(
        stock__gt=0
    )

    return render(
        request,
        "core/home.html",
        {
            "products": products,
        },
    )