# class Mobile:
#     android_version = "Android 15"
    
#     def __init__(self,name,ram,memory):
#         self.name = name
#         self.ram = ram
#         self.memory = memory
        
        
#     def get_laptop_config(self):
#         print(f"Mobile {self.name} has {self.ram}GB RAM and {self.memory}GB Memory")
    
#     @classmethod 
#     def get_version_type(cls):
#         print(f"Android version of mobile is {cls.android_version}") 
    
#     @staticmethod
#     def get_discounted_price(price, discount):
#         final_price = price - (price * discount/100) 
#         ret urn final_price  
        
# redmi = Mobile("redmi c25",8,64)
# oneplus = Mobile("oneplus 10R",16,128)


# Mobile.get_version_type()
# redmi.get_laptop_config()
# oneplus.get_laptop_config()
# print(Mobile.get_discounted_price(20000,10))
        
# ---------------------------------------------------------------------------------------------------------------------------- #

class Cart :
    discount = 20 #Class attributes
    min_value = 200 #Class attributes
    price_dict = {"book": 100, "pen": 10, "notebook": 50} #Class attribute

    def __init__(self):
        self.items = {} #Instance attributes
        
    def add_items(self,item,qty): #Instance method
        self.items[item] = qty
        Cart.cart_count += 1
        print(f"{item} added to cart with quantity {qty}")   

    def get_cart_items(self):
        print("Items in cart are:")
        for item, qty in self.items.items():
            print(f"{item}: {qty}") 
    
    def update_qty(self,item,qty):
        if item in self.items:
            self.items[item] = qty
        else:
            print(f"{item} not found in cart") 

    def delete_item(self,item):
        if item in self.items:
            del self.items[item]
        else:
            print(f"{item} not found in cart")

    def total_price(self,price_dict):
        total = 0
        for item, qty in self.items.items():
            if item in price_dict:
                total += price_dict[item] * qty
            else:
                print(f"Price for {item} not found")
        return total
    
    @classmethod
    def get_discount_price(cls,total_price):
        return total_price - (total_price * cls.discount/100)#Class method
    
    @staticmethod
    def greet():#Static method
        print('Have a nice day')
        
cart_obj = Cart()
cart_obj.add_items("book",3)
cart_obj.add_items("pen",5)
cart_obj.add_items("notebook",2)
cart_obj.get_cart_items()
cart_obj.update_qty("pen",10)
cart_obj.get_cart_items()
cart_obj.delete_item("notebook")
cart_obj.get_cart_items()
print(f"Total price of items in cart is: {cart_obj.total_price(cart_obj.price_dict)}")
print(f"Total price after discount is: {Cart.get_discount_price(cart_obj.total_price(cart_obj.price_dict))}")
cart_obj.greet()


