class Cart :
    discount = 20
    min_value = 200 #Class attributes
    def __init__(self):
        self.items = {} #Instance attributes
        
    def add_items(self,item,qty): #Instance method
        self.items[item] = qty
    
    @classmethod
    def change_discount(cls,disc):#Class method
        discount = disc
    
    @staticmethod
    def greet():#Static method
        print('Have a nice day')
        
cart_obj = Cart()
cart_obj.add_items("book",3)
print(cart_obj.items)
cart_obj.change_discount(38)
print(cart_obj.discount)
cart_obj.greet()