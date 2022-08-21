from shop.products import is_product_in_shop
from shop.order import create_new_order

def start_order():
    print("Witaj w sklepie!")
    new_order = []

    while True:
        product_name = input("Podaj nazwe produktu lub 'X' zeby zakonczyc: ")
        if product_name == "X":
            break

        if not is_product_in_shop(product_name):
            print("Niestety nie mamy takiego produktu.")
        else:
            ordered_quantity = int(input("Podaj ilosc: "))
            order = create_new_order(product_name, ordered_quantity)
            new_order.append(order)

    print(new_order)

if __name__ == '__main__':
    start_order()