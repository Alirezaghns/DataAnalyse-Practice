from models import Product, User


class Store:
    def __init__(self):
        self.products = dict()
        self.users = list()

    def add_products(self, product, amount=1):
        """ Add a product object into prudcts dictionary """
        self.products[product] = self.products.get(product, 0) + amount
    
    def remove_product(self, product, amount=1):
        """ Remove an object from products dictionary """
        if product in self.products.keys():
            if self.products[product] >= amount:
                self.products[product] -= amount
                if self.products[product] == 0:
                    del self.products[product]
            else:
                raise Exception("Not Enough Products!")
        else:
            raise Exception("Not Enough Products!")

    def add_user(self, username):
        """ Add a user into users list """
        new_user = User(username)
        # for user in self.users:
        #     if new_user == user:
        #         return None
        result = [new_user == user for user in self.users]
        if not any(result):
            self.users.append(new_user)
            return username
        return None

    def get_total_asset(self):
        """ Return total asset """
        total_assets = 0
        for product, amount in self.products.items():
            total_assets += product.price * amount
        return total_assets

    def get_total_profit(self):
        """ Return total profit """
        total_profit = 0
        for user in self.users:
            # for product in user.bought_products:
            #     total_profit += product.price
            total_profit += sum([product.price for product in user.bought_products])
        return total_profit

    def get_comments_by_user(self, user):
        """ Return list of all comments written by a user """
        msg = list()
        for product in self.products.keys():
            # msg += [comment.text for comment in product.comments if comment.user == user]
            msg += list(filter(lambda comment: comment.user == user, product.comments))
        return msg

    def get_inflation_affected_product_name(self):
        """ Return the list of all affected products """
        products = list()
        for product in self.products.keys():
            products += [checking_product.name for checking_product in self.products.keys() if product.name == checking_product.name and product.price < checking_product.price]
        products = list(set(products))
        return products

    def clean_old_comments(self, date):
        """ Remove all old comment objects """
        for product in self.products.keys():
            product.comments = filter(lambda comment: comment.date_added > date, product.comments)

    def get_comments_by_bought_users(self, product):
        """ Return comments by bought users """
        msg = list()
        for user in self.users:
            if product in user.bought_products:
                msg += [comment.text for comment in product.comments if comment.user == user]
        return msg

product_1 = Product("laptop", 90_000_000, "electronic")
product_2 = Product("mobile", 15_000_000, "electronic")
product_3 = Product("ipad", 65_000_000, "electronic")

my_store = Store()
print(my_store.products)

my_store.add_products(product_1, 2)
my_store.add_products(product_2)
my_store.add_products(product_3)

print(my_store.products)

my_store.remove_product(product_1, 1)
print(my_store.products)

# my_store.remove_product(product_2, 5)

user_1 = User("David")
user_2 = User("John")

print(my_store.users)
my_store.add_user(user_1)
my_store.add_user(user_2)
print(my_store.users)