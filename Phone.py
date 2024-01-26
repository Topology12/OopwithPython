from Item import Item
class Phone(Item):
    list_phone = []

    def __init__(self, name: str, price: float, quanlity=1, broken_phone=0) -> None:
        assert broken_phone >= 0, f"{broken_phone} invalid"
        super().__init__(name, price, quanlity)
        self.broken_phone = broken_phone

        Phone.list_item.append(self)



