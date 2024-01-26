import csv


class Item:
    # class atrribute
    pay_rate = 0.8
    list_item = []

    def __init__(self, name: str, price: float, quanlity=1) -> None:
        # Xác thực đối số
        assert price >= 0
        assert quanlity >= 0

        self.__name = name
        self.__price = price
        self.__quanlity = quanlity

        Item.list_item.append(self)

    def calculate_total_price(self):
        return self.__quanlity*self.__price

    def apply_discount(self):
        self.__price = self.__price * self.pay_rate

    def __repr__(self):
        return f"Item({self.__name}, {self.__price}, {self.__quanlity})"

    @classmethod
    def instantiate_from_csv(cls):
        with open('item.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
            for item in items:
                Item(name=item.get('name'), price=float(
                    item.get('price')), quanlity=int(item.get("quanlity")))

    @staticmethod
    def is_integer(num):
        if isinstance(num, float):
            return num.is_integer()
        elif num.is_integer():
            return True
        else:
            return False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
