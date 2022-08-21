products = [
    {
        "product": "jablko",
        "quantity": 10,
        "price": 1.2
    },
    {
        "product": "mleko",
        "quantity": 12,
        "price": 5.2
    },
{
        "product": "chleb",
        "quantity": 32,
        "price": 10.2
    }
]

def find_product_by_name(product_name):
    for product in products:
        if product["product"] == product_name:
            return product

def is_product_in_shop(product_name):
    if not find_product_by_name(product_name):
        return False
    return True