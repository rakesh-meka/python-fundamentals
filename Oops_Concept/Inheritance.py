# Inheritance example:
# A common base class and a specific child class extending it

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def login(self):
        print(f"{self.username} logged in")

    def logout(self):
        print(f"{self.username} logged out")


class AdminUser(User):
    def __init__(self, username, email, access_level):
        super().__init__(username, email)
        self.access_level = access_level

    def delete_user(self, user):
        print(f"Admin {self.username} deleted user {user}")


# -------- usage --------
user1 = User("rakesh", "rakesh@gmail.com")
admin1 = AdminUser("admin01", "admin@gmail.com", "full")

user1.login()
user1.logout()

print("-" * 30)

admin1.login()              # inherited from User
admin1.delete_user("test")  # admin-specific action
admin1.logout()