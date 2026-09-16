
class Coffee:
    def __init__(self, size, price):
        # Initialize with provided size and price
        self._size = None
        self._price = None

        # use the property setters to validate
        self.size = size
        self.price = price

    def get_size(self):
        return self._size

    def set_size(self, value):
        # Accept only these specific values (capitalized) as per tests
        if value in ['Small', 'Medium', 'Large']:
            self._size = value
        else:
            # Match expected error message from tests
            print("size must be Small, Medium, or Large")

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
        # Message must match tests (note the curly apostrophe)
        print("This coffee is great, here’s a tip!")
        self._price = self._price + 1


