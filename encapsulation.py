class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password

    @property
    def password(self):
        return self.__password.upper()
    
    @password.setter
    def password(self, value):
        if len(value) > 8:
            self.__password = value



user_1 = User("my_username", "934wurfksf")
# print(user_1.password)
# user_1.password = "wefjfsdknksvcs"
# print(user_1.password)
# print(user_1._User__password)