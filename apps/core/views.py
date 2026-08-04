from django.shortcuts import render, get_object_or_404


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

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)

    return render(
        request,
        "products/detail.html",
        {
            "product": product,
        },
    )