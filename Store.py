from Item import Item
from Phone import Phone

# item1 = Item("Phone", 100, 5)
# print(item1.name)
# item2 = Item("Laptop", 1000, 2)
# print(item2.name)
# item2.pay_rate = 0.1
# item2.apply_discount()
# print(item2.calculate_total_price())
item1 = Item('Phone', 100, 1)
item2 = Item('Laptop', 1000, 3)
item3 = Item('Cable', 10, 5)
item4 = Item('Mouse', 50, 5)
item5 = Item('Keyboard', 75, 5)


# Item.instantiate_from_csv()

# for item in Item.list_item:
#     print(item)
print(Item.is_integer(7.0))
phone1 = Phone("Samsung Galaxy Note 11 Pro", 5000, 1, 0)
print(phone1.name)
phone1.name = "Iphone"
print(phone1.name)