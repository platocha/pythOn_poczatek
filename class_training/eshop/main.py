from shop.order import Order
import random

def get_order_price(order):
    return order.total_price

def run_homework():
    orders = []
    for _ in range(5):
        orders.append(Order.generate_order(random.randint(1,8)))

    orders.sort(key=lambda order: order.total_price)
    for order in orders:
        print(order)

if __name__ == '__main__':
    run_homework()


