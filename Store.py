class Item:

    def __init__(self, name: str, price: float, quanlity=1) -> None:
        # Xác thực đối số
        assert price >= 0
        assert quanlity >= 0
        self.name = name
        self.price = price
        self.quanlity = quanlity

    def calculate_total_price(self):
        return self.quanlity*self.price


item1 = Item("Phone", 100, 5)
print(item1.name)

item2 = Item("Laptop", 1000, 2)
print(item2.name)
print(item2.calculate_total_price())
