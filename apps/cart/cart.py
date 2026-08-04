from apps.products.models import Product

class Cart:

    def __init__(self, request):
        self.session = request.session

        cart = self.session.get("cart")

        if not cart:
            cart = self.session["cart"] = {}

        self.cart = cart
    
    def save(self):
        self.session.modified = True

    def add(self, product, quantity=1):
        product_id = str(product.id)

        if product_id not in self.cart:

            self.cart[product_id] = {
                "quantity": 0,
            }

        self.cart[product_id]["quantity"] += quantity

        self.save()

    def get_total_price(self):
        return sum(
            item["total_price"]
            for item in self
        )

    def remove(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            del self.cart[product_id]
            self.save()
    
    def clear(self):
        self.session.pop("cart", None)
        self.save() 

    def update(self, product, quantity):
        product_id = str(product.id)

        if product_id in self.cart:
            if quantity > 0:
                self.cart[product_id]["quantity"] = quantity
            else:
                del self.cart[product_id]

            self.save()
        
    def decrease(self, product):
        product_id = str(product.id)

        if product_id in self.cart:
            if self.cart[product_id]["quantity"] > 1:
                self.cart[product_id]["quantity"] -= 1
            else:
                del self.cart[product_id]

            self.save()

    def __len__(self):
        return sum(
            item["quantity"]
            for item in self.cart.values()
        )

    def __iter__(self):
        product_ids = self.cart.keys()

        products = Product.objects.filter(
            id__in=product_ids
        )

        cart = self.cart.copy()

        for product in products:
            cart[str(product.id)]["product"] = product

        for item in cart.values():

            product = item["product"]

            item["price"] = product.price

            item["total_price"] = (
                product.price * item["quantity"]
            )

            yield item