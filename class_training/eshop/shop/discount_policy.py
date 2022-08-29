class DiscountPolicy:

    def apply_discount(self, total_price):
        return total_price

class PercentageDiscount(DiscountPolicy):

    def __init__(self, percentage):
        self.percentage = percentage

    def apply_discount(self, total_price):
        return total_price * (100 - self.percentage) / 100

class AbsoluteDiscount(DiscountPolicy):

    def __init__(self, discount_value):
        self.discount_value = discount_value

    def apply_discount(self, total_price):
        if self.discount_value > total_price:
            return 0
        return total_price - self.discount_value
