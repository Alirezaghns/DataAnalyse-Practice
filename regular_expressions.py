import re

class Email:
    def __init__(self, email):
        self.email = email
        self.is_valid = self.validate_email()
    
    def validate_email(self):
        pattern = r"^\w+@\w+.com$"
        return bool(re.search(pattern, self.email))
    
    def __str__(self):
        return f"{self.email} validation is {self.is_valid}"
    

email = input("Enter your email: ")
first_email = Email(email)
print(first_email)