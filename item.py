import csv


class Item:
    pay_rate = 0.8 # The pay rate after 20% dicsount(class attribute)

    all = []

    def __init__(self,name:str,price:float,quantity = 0):
        # print(f"An instance Created:{name}")
        # Run Validatiions to the received Arguments

        assert price >= 0, f"Price {price} should be grater or == 0"
        assert quantity >= 0, f"Quantity {quantity} should be grater or == 0"

        #Assign to self Object
        self.__name = name
        self.price = price
        self.quantity = quantity

        # Actions to execute
        Item.all.append(self)
    @property
    #property Decorator = Read-Only Attribute
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        self.__name = value

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price =  self.price * self.pay_rate


    @classmethod
    def instantiate_from_csv(cls):
        with open('items.csv','r') as f:
            reader = csv.DictReader(f)
            items = list(reader)
        
        for item in items:
            # print(item)
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        # for i.e: 5.0, 10.0
        if isinstance(num,float):
            #Count out the floats that are point zero
            return num.is_integer()
        elif isinstance(num,int):
            return True
        else:
            return False


    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self.name}',{self.price,self.quantity})"
    

