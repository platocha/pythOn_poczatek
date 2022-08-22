from shop.apple import Apple
from shop.order import print_order, generate_order
from shop.potato import Potato

def run_homework():
    green_apple = Apple(species="Green", size="M", price=3.5)
    red_apple = Apple(species="Red", size="S", price=2.8)
    print(green_apple.species, green_apple)
    print(red_apple.species, red_apple)

    old_potato = Potato(species="Potato Old", size="S", price=0.8)
    print(old_potato.species, old_potato)

    first_order = generate_order()
    print_order(first_order)
    second_order = generate_order()
    print_order(second_order)

if __name__ == '__main__':
    run_homework()



