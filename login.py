
class Login:
    def __init__(self):
        self.id = "Admin1234"
        self.password = "Admin"
        self.max_attempts = 3

    def login(self):
        for attempt in range(self.max_attempts):
            user_id = input("Enter the ID: ")
            password = input("Enter the password: ")

            if user_id == self.id and password == self.password:
                print("Login successful!")
                return True

            if user_id != self.id:
                print("Incorrect ID.")
            else:
                print("Incorrect password.")

            remaining = self.max_attempts - (attempt + 1)

            if remaining > 0:
                print("Remaining attempts:", remaining)

        print("Too many failed attempts. Access denied!")
        return False
