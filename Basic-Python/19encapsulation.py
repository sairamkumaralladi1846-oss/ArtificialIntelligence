class Account:
    def __init__(self, name,account_number, balance):
        self.name = name
        self._account_number = account_number  # Protected attribute
        self.__balance = balance  # Private attribute

    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.") 
    
    def get_account_number(self):
        return self._account_number 
    

acc = Account("John Doe", "123456789", 1000)
# Accessing protected attribute (not recommended, but possible)
print(f"Account Number: {acc._account_number}")  # Accessing protected attribute
# Accessing protected attribute using getter method
print(f"Account Number (using getter): {acc.get_account_number()}")  # Accessing protected attribute using getter method
# Accessing private attribute (will raise an error)
#print(f"Balance: {acc.__balance}")  # This will raise an AttributeError
# Accessing private attribute using getter method
print(f"Balance: {acc.get_balance()}")  # Accessing private attribute using getter method
# Depositing money
acc.deposit(500)  # Depositing money
print(f"Balance after deposit: {acc.get_balance()}")  # Checking balance after deposit
# Accessing private attribute directly (Not recommended, but possible using name mangling)
print(f"Balance (using name mangling): {acc._Account__balance}")  # Accessing private attribute using name mangling
