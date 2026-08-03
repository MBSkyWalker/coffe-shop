from django.shortcuts import render

from apps.products.models import Product


def home(request):

    products = Product.objects.filter(show_on_homepage=True).order_by("-created_at")[:6]

    return render(
        request,
        "core/home.html",
        {
            "products": products,
        },
    )