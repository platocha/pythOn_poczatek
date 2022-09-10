from shop.errors import TemporaryOutOfStock, ProductNotAvailable, NotValidInput
from shop.order import Order
from shop.store import Store
import os


def handle_customer():
    say_hello()
    order = init_order()
    while want_more_products():
        add_product_to_order(order, Store.AVAILABLE_PRODUCTS)
    print_order_summary(order)
    save_orders_to_file(order)


def say_hello():
    print("Witaj w naszym sklepie!")


def init_order():
    first_name = input("Podaj imie: ")
    last_name = input("Podaj nazwisko: ")
    return Order(client_first_name=first_name, client_last_name=last_name)


def want_more_products():
    selection = input("Czy chcesz dodać produkty do zamówienia? T/N: ")
    if selection.upper() != "T" and selection.upper() != "N":
        print("Opcje są tylko dwie - zakładam, że chcesz coś zamówić ;)")
        return True
    return selection.upper() == "T"


def add_product_to_order(order, available_products):
    print("Oto dostępne produkty:")
    for index, available_product in enumerate(available_products):
        print(f"{index}) {available_product.product}")

    try:
        product_index_str = input("Wybierz numer: ")
        product_index = parse_product_index(product_index_str, max_index=len(available_products) - 1)

        quantity_str = input("Podaj liczbę sztuk: ")
        quantity = parse_quantity(quantity_str)
    except NotValidInput as input_error:
        print(input_error)
        return

    try:
        order.add_product_to_order(available_products[product_index].product, quantity)
    except TemporaryOutOfStock as error:
        print(f"Niestety mamy dostępne tylko {error.available_quantity} sztuk produktu {error.product_name}")
    except ProductNotAvailable as error:
        print(f"Produkt {error.product_name} nie jest dostępny. Wybierz inny.")


def parse_product_index(product_index_str, max_index):
    try:
        product_index = int(product_index_str)
    except ValueError:
        raise NotValidInput("Numer produktu musi byc liczba.")

    if 0 > product_index > max_index:
        raise NotValidInput(f"Numer produktu musi miescic sie w przedziale 0 - {max_index}")

    return product_index

def parse_quantity(quantity_str):
    try:
        quantity = int(quantity_str)
    except ValueError:
        raise NotValidInput("Ilosc musi byc liczba")

    if quantity < 1:
        raise NotValidInput("Ilosc musi byc wieksza od 0")

    return quantity

def save_orders_to_file(order):
    orders_data_file_path = os.path.join("data", "orders.txt")
    with open(orders_data_file_path, mode="w") as orders_file:
        orders_file.write(str(order))


def print_order_summary(order):
    print("Twoje zamówienie to:")
    print(order)
    print("Dziękujemy i zapraszamy ponownie!")
