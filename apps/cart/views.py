from django.shortcuts import get_object_or_404, redirect, render

from apps.products.models import Product

from .cart import Cart


def cart_add(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(
        Product,
        id=product_id,
    )

    cart.add(product)
    prod = get_object_or_404(Product, id=product_id)
    print(prod)
    return redirect("home")


def cart_detail(request):
    return render(
        request,
        "cart/detail.html",
    )

def cart_increase(request, product_id):

    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)

    cart.add(product)

    return redirect("cart:cart_detail")

def cart_decrease(request, product_id):

    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)

    cart.decrease(product)

    return redirect("cart:cart_detail")


def cart_remove(request, product_id):

    cart = Cart(request)

    product = get_object_or_404(Product, id=product_id)

    cart.remove(product)

    return redirect("cart:cart_detail")