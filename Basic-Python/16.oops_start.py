class Cart:
    def __init__(self):
        self.items={}
        self.price_det = {"book":100,"laptop":35000,"mouse":200}

    def add_item(self,item,quantity):
        self.items[item] = quantity
        
    def get_items(self):
        for item, qty in self.items.items():
            print(f'Your cart details:\n{item}:{qty}')
            
    def delete_item(self,item):
        del self.items[item]
        print(f'item {item} is deleted from your cart')
    
    def total_price(self):
        price = 0
        print('Your cart details:')
        for item, qty in self.items.items():
            print(f'{item}-->{qty}')
            price+=qty*self.price_det[item]
        print(f'total_price---->{price}') 
        
cart_obj = Cart()

cart_obj.add_item('book',3)
cart_obj.add_item('laptop',2)
cart_obj.get_items()
cart_obj.total_price()
cart_obj.delete_item('book')
cart_obj.get_items()