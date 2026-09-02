
class Coffee:
    def __init__(self):
        # Prompt customer for input
        size_input = input("Enter the size of the coffee (small, medium, large): ")
        price_input = float(input("Enter the price of the coffee: "))

        self._size = None
        self._price = None

        self.set_size(size_input)
        self.set_price(price_input)

    def get_size(self):
        return self._size

    def set_size(self, value):
        if value in ['small', 'medium', 'large']:
            self._size = value
        else:
            print("Invalid size. Please choose 'small', 'medium', or 'large'.")

    size = property(get_size, set_size)

    def get_price(self):
        return self._price

    def set_price(self, value):
        if value >= 0:
            self._price = value
        else:
            print("Invalid price. Please enter a positive value.")

    price = property(get_price, set_price)

    def tip(self):
        print("This coffee is great, here's a tip!")
        self._price = self._price + 1


