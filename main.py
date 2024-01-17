# item1= 'Phone'
# item1_price = 100
# item1_quantity = 5
# item1_price_total = item1_price * item1_quantity

# print(type(item1)) #str
# print(type(item1_price)) #int
# print(type(item1_quality)) #int
# print(type(item1_price_total)) #int

class Item:
    def __init__(self,name):
        print(f"An instance Created:{name}")
    def calculat_total_price(self,x,y):
        return x * y


item1 = Item("Phone")
# item1.name = "Phone"
item1.price = 100
item1.quantity = 5
# print(item1.calculat_total_price(item1.price,item1.quantity))

item2 = Item("Laptop")
# item2.name = "Laptop"
item2.price = 1000
item2.quantity = 3
# print(item2.calculat_total_price(item2.price,item2.quantity))

# print(type(item1))
# print(type(item1.name))
# print(type(item1.price))
# print(type(item1.quantity))

# random_str = "aaa"
# print(random_str.upper())