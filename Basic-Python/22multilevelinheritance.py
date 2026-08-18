class Product:
    def __init__(self, name, price, deal_price, ratings):
        self.name = name
        self.price = price
        self.deal_price = deal_price
        self.ratings = ratings

    def display_product_details(self):
        print(f"Product: {self.name}")
        print(f"Price: {self.price}")
        print(f"Deal Price: {self.deal_price}")
        print(f"You Saved: {self.price - self.deal_price}")
        print(f"Ratings: {self.ratings}")

    def get_save_amount(self):
        return self.price - self.deal_price

class ElectronicItem(Product):
    def __init__(self, name, price, deal_price, ratings, warranty_in_months):
        super().__init__(name, price, deal_price, ratings)
        self.warranty_in_months = warranty_in_months 

    def display_product_details(self):
        super().display_product_details() 
        print(f"Warranty: {self.warranty_in_months} months") 

class Laptop(ElectronicItem):
    def __init__(self, name, price, deal_price, ratings, warranty_in_months, processor):
        super().__init__(name, price, deal_price, ratings, warranty_in_months)
        self.processor = processor 

    def display_product_details(self):
        super().display_product_details() 
        print(f"Processor: {self.processor}")

laptop = Laptop("Gaming Laptop", 150000, 120000, 4.5, 24, "Intel i7")
laptop.display_product_details()
print(f"Amount Saved: {laptop.get_save_amount()}")

# Product: Gaming Laptop
# Price: 150000
# Deal Price: 120000
# You Saved: 30000
# Ratings: 4.5
# Warranty: 24 months
# Processor: Intel i7
# Amount Saved: 30000