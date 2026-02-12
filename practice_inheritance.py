class User:
    def __init__(self, email, username, password):
        self.email = email
        self.username = username
        self.password = password
        self.is_logged_in = False
    
    def login(self, username, password):
        if self.username == username and self.password == password:
            self.is_logged_in = True
            print("You are logged in now")
        else:
            self.is_logged_in = False
            print("Username or password is not correct")
    
    def introduce(self):
        return f"{self.username} - {self.email}"
    
    def __str__(self):
        return self.introduce()


class Admin(User):
    def __init__(self, email, username, password, level="Normal"):
        super().__init__(email, username, password)
        self.level = level

    def add_product(self, product_name, product_price):
        if self.is_logged_in:
            print(f"A new product with {product_name} title and {product_price} has been added")
        else:
            print("You must be logged in to add a new product")


class Client(User):
    def __init__(self, email, username, password, credit):
        super().__init__(email, username, password)
        self.credit = credit
    
    def introduce(self):
        return f"{self.email} - {self.username} - {self.credit}"
    
    def pay_shopping_card(self, shopping_card_price):
        if self.is_logged_in:
            if self.credit > shopping_card_price:
                self.credit -= shopping_card_price
                print("Your shopping card has been payed")
            else:
                print("You do not have enough credit to pay your shopping card")
        else:
            print("You must be logged in")


user_1 = User("user@gmail.com", "new_user1", "This_is#my@password")

admin_1 = Admin("admin1@gmail.com", "first_admin", "New_random_pass")
admin_1.login("first_admin", "New_random_pass")
admin_1.add_product("Microphone", 39)

client_1 = Client("client@gmail.com", "first_client", "A_valid_pass", 5000)
client_1.login("first_client", "A_valid_pass")
client_1.pay_shopping_card(4000)
print(client_1.password)