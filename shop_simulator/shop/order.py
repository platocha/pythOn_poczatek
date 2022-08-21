from shop.products import find_product_by_name

def create_new_order(product_name, ordered_quantity):
    product = find_product_by_name(product_name)
    order = {
        "product": product["product"],
        "quantity": ordered_quantity,
        "price": product["price"] * ordered_quantity
    }
    return order