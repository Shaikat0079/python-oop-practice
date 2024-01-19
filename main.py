# # item1= 'Phone'
# # item1_price = 100
# # item1_quantity = 5
# # item1_price_total = item1_price * item1_quantity

# # print(type(item1)) #str
# # print(type(item1_price)) #int
# # print(type(item1_quality)) #int
# # print(type(item1_price_total)) #int
# import csv


# class Item:
#     pay_rate = 0.8 # The pay rate after 20% dicsount(class attribute)

#     all = []

#     def __init__(self,name:str,price:float,quantity = 0):
#         # print(f"An instance Created:{name}")
#         # Run Validatiions to the received Arguments

#         assert price >= 0, f"Price {price} should be grater or == 0"
#         assert quantity >= 0, f"Quantity {quantity} should be grater or == 0"

#         #Assign to self Object
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#         # Actions to execute
#         Item.all.append(self)


#     def calculate_total_price(self):
#         return self.price * self.quantity

#     def apply_discount(self):
#         self.price =  self.price * self.pay_rate


#     @classmethod
#     def instantiate_from_csv(cls):
#         with open('items.csv','r') as f:
#             reader = csv.DictReader(f)
#             items = list(reader)
        
#         for item in items:
#             # print(item)
#             Item(
#                 name=item.get('name'),
#                 price=float(item.get('price')),
#                 quantity=int(item.get('quantity'))
#             )

#     @staticmethod
#     def is_integer(num):
#         # We will count out the floats that are point zero
#         # for i.e: 5.0, 10.0
#         if isinstance(num,float):
#             #Count out the floats that are point zero
#             return num.is_integer()
#         elif isinstance(num,int):
#             return True
#         else:
#             return False


#     def __repr__(self) -> str:
#         return f"{self.__class__.__name__}('{self.name}',{self.price,self.quantity})"



# class Phone(Item):


#     def __init__(self, name: str, price: float, quantity=0,broken_phones = 0):
#         # Call to the super function to have access to all attributes/methods
#         super().__init__(name, price, quantity)
#         self.broken_phones = broken_phones
#         # assert price >= 0, f"Price {price} should be grater or == 0"
#         # assert quantity >= 0, f"Quantity {quantity} should be grater or == 0"
#         assert broken_phones >=0, f"Borken phones {broken_phones} should be grater or == 0"
        


# # item1 = Item("Phone",100,-1)
# # item1 = Item("Phone",100,5) # Class er instance
# # item1.name = "Phone"
# # item1.price = 100
# # item1.quantity = 5
# # print(item1.calculate_total_price(item1.price,item1.quantity))

# # item2 = Item("Laptop",1000,3)
# # item2.name = "Laptop"
# # item2.price = 1000
# # item2.quantity = 3
# # print(item2.calculate_total_price(item2.price,item2.quantity))


# # print(item1.name)
# # print(item1.price)
# # print(item1.quantity)
# # print(item2.name)
# # print(item2.price)
# # print(item2.quantity)
# # item2.has_numpad = False


# # print(type(item1))
# # print(type(item1.name))
# # print(type(item1.price))
# # print(type(item1.quantity))

# # random_str = "aaa"
# # print(random_str.upper())

# # print(item1.calculate_total_price())
# # print(item2.calculate_total_price())


# # print(Item.pay_rate) # This is class attribute
# # print(item1.pay_rate) # This is class attribute they got the value from class level
# # print(item2.pay_rate) # This is class attribute they got the value from class level

# # print(Item.__dict__) # All the attribute for the class level
# # print(item1.__dict__) # All the attribute for the instance level

# # item1.apply_discount()
# # print(item1.price)
# # item2.apply_discount()
# # print(item2.price)

# # item2.pay_rate = 0.7
# # item2.apply_discount()
# # print(item2.price)




# # print(Item.all)

# # for instance in Item.all:
# #     print(instance.name)




# # print(Item.all)

# # Item.instantiate_from_csv()
# # print(Item.all)
# # print(Item.is_integer(7))
# # print(Item.is_integer(7.0))
# # print(Item.is_integer(7.5))

# phone1 = Phone("iPhone14",1300,5,1)
# # phone1.broken_phones = 1
# phone2 = Phone("iPhone15",1400,5,1)
# # phone2.broken_phones = 1

# print(phone1.calculate_total_price())

# print(Item.all)

# print(Phone.all)

from item import Item
from phone import Phone

# Item.instantiate_from_csv()

# print(Item.all)

item1 = Item("MyItem",750)
print(item1.name)
#setting Attribute
item1.name = "OtherTeam"
#Getting attribute
print(item1.name)