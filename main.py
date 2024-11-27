class BankAccount:
    def __init__(self, holder_name: str, initial_balance: float):
        self.holder_name = holder_name
        self.balance = initial_balance
        
        print(f"Account created for {self.holder_name} with balance: {self.balance:.2f}")
        
    def deposit(self, amount: float):
         if amount > 0:
             self.balance += amount
             print(f"Deposited {amount:.2f} to account. New balance: {self.balance:.2f}")
         else:
             print("Invalid deposit amount. Please enter a positive value.")
    
    def withdraw(self, amount: float):
         if amount > 0 and amount <= self.balance:
             self.balance -= amount
             print(f"Withdrew {amount:.2f} from account. New balance: {self.balance:.2f}")
         else:
             print("Invalid withdrawal amount. Please enter a positive value and ensure sufficient balance.")
             
    def get_balance(self):
         return self.balance

if __name__ == "__main__":
    
    account = BankAccount("Tanvir", 5000.0)
    account.deposit(2000.0)
    account.withdraw(1500.0)
    print(f"Account balance: {account.get_balance():.2f}")
