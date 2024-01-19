from item import Item
class Phone(Item):


    def __init__(self, name: str, price: float, quantity=0,broken_phones = 0):
        # Call to the super function to have access to all attributes/methods
        super().__init__(name, price, quantity)
        self.broken_phones = broken_phones
        # assert price >= 0, f"Price {price} should be grater or == 0"
        # assert quantity >= 0, f"Quantity {quantity} should be grater or == 0"
        assert broken_phones >=0, f"Borken phones {broken_phones} should be grater or == 0"
        




phone1 = Phone("iPhone14",1300,5,1)
# phone1.broken_phones = 1
phone2 = Phone("iPhone15",1400,5,1)
# phone2.broken_phones = 1

print(phone1.calculate_total_price())

print(Item.all)

print(Phone.all)