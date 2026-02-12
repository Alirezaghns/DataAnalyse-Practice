class Wallet:
    def __init__(self, initial_balance):
        self.balance = initial_balance

    def get_balance(self):
        print(f"You have {self.balance}$ in your wallet")
    
    def __str__(self):
        return f"This wallet contains {self.balance}$"
    
    def __add__(self, other):
        return self.balance + other.balance

    def __sub__(self, other):
        return self.balance - other.balance
    
    def __mul__(self, other):
        return self.balance * other.balance
    
    def __eq__(self, other):
        return self.balance == other.balance
    
    def __lt__(self, other):
        return self.balance < other.balance
    
    def __gt__(self, other):
        return self.balance > other.balance
    
    def __ne__(self, other):
        return self.balance != other.balance
    
    def __len__(self):
        return self.balance


wallet_1 = Wallet(100)
wallet_2 = Wallet(50)

attr = "balance"

# print(setattr(wallet_1, attr, 500))
# print(wallet_1)

# print(hasattr(wallet_1, "user"))